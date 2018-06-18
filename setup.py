
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from os import path

from io import open

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()


with open('LICENSE') as f:
  license = f.read()

setup(
    name='xspeedit',
    version='0.1.0',
    description='Python package to pack items',
    long_description=long_description,
    author='Hardik Juneja',
    author_email='hardikjuneja.hj@gmail.com',
    url='https://github.com/hardikj/xspeedit',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
