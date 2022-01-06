# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='convpybayes',
    version='0.0.1',
    description='Bayesian model for lagged conversion estimation.',
    author='Alexander Volkmann',
    author_email='alexv@gmx.de',
    packages=find_packages(),
    setup_requires=['pytest-runner>=4.2', 'flake8'],
    install_requires=[i.strip() for i in open("requirements.txt").readlines()],
    tests_require=['pytest>=4.0.2', 'pytest-cov>=2.6.0', 'pytest-watch>=4.2.0']
)
