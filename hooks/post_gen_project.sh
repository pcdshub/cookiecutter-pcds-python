#!/bin/bash
{% if cookiecutter.auto_git_setup == "yes" %}
git init
git add -A
git remote add {{ cookiecutter.git_remote_name }} git@github.com:{{ cookiecutter.github_repo_group }}/{{ cookiecutter.repo_name }}.git
{% endif %}
{% if cookiecutter.auto_versioneer_setup == "yes" %}
pip install versioneer
versioneer install
{% endif %}
