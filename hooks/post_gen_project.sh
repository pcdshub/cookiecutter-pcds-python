#!/bin/bash
{% if cookiecutter.auto_git_setup == "yes" %}
git init
git add -A
git remote add {{ cookiecutter.git_remote_name }} git@github.com:{{ cookiecutter.github_repo_group }}/{{ cookiecutter.repo_name }}.git
git commit -am "Initial commit from cookiecutter-pcds-python"
{% endif %}
