"""
Setup script for dais_sthlm23.

This script packages and distributes the associated wheel file(s).
Source code is in ./src/. Run 'python setup.py sdist bdist_wheel' to build.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import dais_sthlm23

setup(
    name="dais_sthlm23",
    version=dais_sthlm23.__version__,
    url="https://databricks.com",
    author="gustav.byberg@databricks.com",
    description="my test wheel",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={"entry_points": "main=dais_sthlm23.main:main"},
    install_requires=["setuptools"],
)
