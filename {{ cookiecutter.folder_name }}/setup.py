import versioneer
from setuptools import setup, find_packages

setup(name='{{ cookiecutter.repo_name }}',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      license='BSD',
      author='{{ cookiecutter.author_name }}',
      packages=find_packages(),
      description='{{ cookiecutter.description }}',
      )
