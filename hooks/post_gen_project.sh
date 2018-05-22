#!/bin/bash
{% if cookiecutter.auto_git_setup == "yes" %}
git init
git add -A
git remote add upstream https://github.com/{{ cookiecutter.github_repo_group }}/{{ cookiecutter.repo_name }}.git
{% endif %}
{% if cookiecutter.auto_versioneer_setup == "yes" %}
versioneer install
{% endif %}
{% if cookiecutter.auto_doctr_setup == "yes" %}
doctr configure 
{% endif %}

