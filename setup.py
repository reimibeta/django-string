#!/usr/bin/env python


import os

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

import setuptools

setuptools.setup(
    name='string_randoms',
    version='1.0.1',
    packages=setuptools.find_packages()
)
