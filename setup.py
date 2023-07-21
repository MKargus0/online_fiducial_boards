# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='online_fiducial_boards',
    version='0.1.0',
    description='Online fiducial generator package',
    long_description=readme,
    author='MKargus0',
    author_email='colodochca@gmail.com',
    packages=find_packages(exclude=('tests'))
)