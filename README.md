[![CI](https://github.com/jmandrake/pypi-package-template/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/jmandrake/pypi-package-template/actions/workflows/cicd.yml)

## Video How-To / Intro to packages
https://www.youtube.com/watch?v=JkeNVaiUq_c

## Templates for Pypi packages
1) Create an account at https://pypi.org/
2) Clone this repo
3) Python package: How to create a new Python Package / Module

pip install twine

python setup.py sdist bdist_wheel

twine upload dist/*

## Update the package and reupload after updating setup.py:
python setup.py sdist bdist_wheel
twine upload dist/*


Testing the package with PIP:

pip install YOURPACKAGE

pip install YOURPACKAGE --upgrade


### Testing package locally
cd to project folder, then pip install the current package locally:
pip install .

# install local source without making a copy?
pip install -e .

ipython 
>>> from mypackage import testfilename
>>> exit()

## Build the package:
python -m build

## Upload to test.pypi.org (test the build before uploading to production)
python -m twine upload -repository testpypi dist/*
## Remove the local package:
pip uninstall packagename
## Reinstall the package from test.pypi.org
pip install -i https://test.pypi.org/simple/ mypackagename



### MANIFEST file
pip install check-manifest
check-manifest --create
git add -A



## Generated from Template for Python project

1. First thing to do on launch is to open a new shell and verify virtualenv is sourced.

Things included are:

* `Makefile`

* `Pytest`

* `pandas`

* `Pylint`

* `Dockerfile`

* `GitHub copilot`

* `jupyter` and `ipython` 

* A base set of libraries for devops and web

* `githubactions` 

