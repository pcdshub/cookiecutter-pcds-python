===============
Getting started
===============

Requirements for the Template
-----------------------------
- Python >= 3.5
- `Cookiecutter Python package <http://cookiecutter.readthedocs.org/en/latest/installation.html>`_ >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages: 

::

  $ pip install cookiecutter


or ::

  $ conda install cookiecutter -c conda-forge


Starting a New Project
----------------------

If using for the first time or in need of a new clone: ::

  $ cookiecutter https://github.com/apra93/cookiecutter-data-science-apra

Otherwise: ::

  $ cookiecutter cookiecutter-data-science-apra


Resulting Directory Structure
-----------------------------

The directory structure of your new project looks like this: 

.. code-block:: text

  ├── {{ import_name }}  <- Source code for use in this project.
  │   │
  │   ├── __init__.py    <- Makes src a Python module
  │   │
  │   ├── data           <- Scripts to download or generate data
  │   │   └── make_dataset.py
  │   │
  │   ├── features       <- Scripts to turn raw data into features for modeling
  │   │   └── build_features.py
  │   │   └── preprocessing.py
  │   │
  │   ├── models         <- Scripts to train models and then use trained models to make
  │   │   │                 predictions
  │   │   ├── predict_model.py
  │   │   └── train_model.py
  │   │
  │   ├── utils.py       <- Utility functions used throughout the repo
  │   │
  │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
  │       └── visualize.py
  │   
  ├── data
  │   ├── external       <- Data from third party sources
  │   ├── interim        <- Intermediate data that has been transformed
  │   ├── processed      <- The final, canonical data sets for modeling
  │   └── raw            <- The original, immutable data dump
  │
  ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
  │   
  ├── figures
  │   ├── finalized      <- Figures that have been polished and should not be changed
  │   └── unsorted       <- Unsorted figures that are not version controlled
  │
  ├── docs               <- Directory for log files and is not  version controlled
  │
  ├── models             <- Trained and serialized models, model predictions, or model summaries
  │
  ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
  │                         the creator's initials, and a short `-` delimited description, e.g.
  │                         `1.0-jqp-initial-data-exploration`
  │
  ├── references         <- Data dictionaries, manuals, and all other explanatory materials
  │
  ├── .coveragerc        <- Coveragerc file when running coverage
  │
  ├── .gitignore         <- Gitignore for the repo
  │
  ├── .landscape.yml     <- Yaml file for Landscape continuous code metrics
  │
  ├── .travis.yml        <- Yaml file for travis continuous integration
  │
  ├── LICENSE            <- Licence for the project
  │
  ├── Makefile           <- Makefile with commands like `make data` or `make train`
  │
  ├── MANIFEST.in        <- Manifest file for versioneer
  │
  ├── README.md          <- The top-level README for developers using this project
  │
  ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
  │                         generated with `pip freeze > requirements.txt`
  │
  ├── run_tests.py       <- Script that runs the files in the tests directory
  │
  ├── setup.cfg          <- Setup file for versioneer
  │
  ├── setup.py           <- `setup.py` file configured to use versioneer
  │
  └── versioneer.py      <- Versioneer source file


Installing Development Requirements
-----------------------------------
::

  $ pip install -r requirements.txt

Running the Tests
-----------------
::

  $ python run_tests.py
