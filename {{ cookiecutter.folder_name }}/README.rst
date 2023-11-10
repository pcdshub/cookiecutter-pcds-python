===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://github.com/{{ cookiecutter.github_repo_group }}/{{ cookiecutter.repo_name }}/actions/workflows/standard.yml/badge.svg
        :target: https://github.com/{{ cookiecutter.github_repo_group }}/{{ cookiecutter.repo_name }}/actions/workflows/standard.yml

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.repo_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.repo_name }}


`Documentation <https://{{ cookiecutter.github_repo_group }}.github.io/{{ cookiecutter.repo_name}}/>`_

{{ cookiecutter.description }}

Requirements
------------

* Python 3.9+

Installation
------------

::

  $ pip install .

Running the Tests
-----------------
::

  $ pytest -v
