#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Kamal McDermott",
    author_email='kamal.mcdermott@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python library with syntax sugar classes/operations",
    entry_points={
        'console_scripts': [
            'phenotype=phenotype.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='phenotype',
    name='phenotype',
    packages=find_packages(include=[
        'phenotype', 
            'phenotype.Access', 
            'phenotype.Assignment',
            'phenotype.Collection',
            'phenotype.Core',
            'phenotype.Func',
            'phenotype.Interfaces',
            'phenotype.Predicate',
            'phenotype.Result',
            'phenotype.States',
            'phenotype.System',
            'phenotype.Text'
            ]),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/dospac87/phenotype',
    version='0.1.0',
    zip_safe=False,
)
