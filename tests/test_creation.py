############
# Standard #
############
import os
import shutil
from pathlib import Path

###############
# Third Party #
###############
import pytest
import simplejson as sjson
from cookiecutter import main

CCDSA_ROOT = os.path.abspath(
                os.path.join(
                    __file__,
                    os.pardir,
                    os.pardir
                )
            )
TEMPLATE_DIR = Path(CCDSA_ROOT) / "{{ cookiecutter.repo_name }}"
CC_JSON = sjson.load(open(str(Path(CCDSA_ROOT) / "cookiecutter.json")))

@pytest.fixture(scope='function')
def default_baked_project(tmpdir):
    out_dir = str(tmpdir.mkdir('data-project'))

    main.cookiecutter(
        CCDSA_ROOT,
        no_input=True,
        extra_context={},
        output_dir=out_dir
    )

    # default project name is project_name
    yield os.path.join(out_dir, 'project_name')

    # cleanup after
    shutil.rmtree(out_dir)

def substitute_cookiecutter_json(name_tuple):
    """
    Substitutes the cookiecutter template names with their values from the json
    file.
    """
    substituted = []
    for part in name_tuple:
        # Check if the cookiecutter braces are in the name
         if "{{ " in part and " }}" in part:
             # Remove them if they are along with 'cookiecutter.'
             part_temp = part.replace("{{ ", "")
             part_temp = part_temp.replace(" }}", "")
             part_temp = part_temp.replace("{{", "")
             part_temp = part_temp.replace("}}", "")
             part_temp = part_temp.replace("cookiecutter.", "")
             # Replace with the json value
             if part_temp in CC_JSON.keys():
                 substituted.append(CC_JSON[part_temp])
                 continue
         else:
             substituted.append(part)
    return substituted

def get_contents(root_dir=TEMPLATE_DIR, omitted_dirs=set([
        ".git", ".cache", "__pycache__", ".ipynb_checkpoints"]),
                 omitted_files=set([])):
    """
    Returns two lists of directories and files of the cookiecutter template
    directory.
    """
    dirs, files = [], []
    # Iterate through all contents of root_dir
    for path in root_dir.iterdir():
        # Only include the parts of the path that come after the template
        # directory name
        expected_path = Path("/".join(path.parts[path.parts.index(
            TEMPLATE_DIR.name)+1:]))
        # Make any substitutions that could be necessary
        substituted_path = "/".join(substitute_cookiecutter_json(
            expected_path.parts))
        # Check if it is a directory that isnt supposed to be omitted
        if path.is_dir() and path.name not in omitted_dirs:
            dirs.append(substituted_path)
            # Go into the directory and get the contents
            dirs_recurse, files_recurse = get_contents(root_dir=path)
            # Update with what we got
            dirs += dirs_recurse
            files += files_recurse
        # If it is a file, check it isnt being omitted
        elif path.is_file() and path.name not in omitted_files:
            files.append(substituted_path)
    return dirs, files

expected_directories, expected_files = get_contents()

@pytest.mark.parametrize("path", expected_directories)
def test_folder(default_baked_project, path):
    path_expected_dir = Path(default_baked_project) / path
    assert path_expected_dir.exists()
    assert path_expected_dir.is_dir()

def no_curlies(filepath):
    """
    Utility to make sure no curly braces appear in a file. That is, was jinja
    able to render everthing?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)

@pytest.mark.parametrize("expected_file", expected_files)
def test_file(default_baked_project, expected_file):
    path_expected_file = Path(default_baked_project) / expected_file
    assert path_expected_file.exists()    
    assert path_expected_file.is_file()
    assert no_curlies(str(path_expected_file))


