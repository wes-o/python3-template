#!/usr/bin/env python

import os
from setuptools import setup, find_packages

h = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(h, 'README.md')) as f:
    README = f.read()

REQUIREMENTS = [
]

setup(
    name='another-python3-template',
    version='0.0.1',
    description='Template syntax with Setuptools',
    long_description=README,
    author='Wes Oler',
    author_email='wes-o@github',
    url='https://github.com/wes-o/python3-template',
    license="Mozilla 2.0",
    install_requires=REQUIREMENTS,
    keywords=['template', 'setuptools'],
    packages=['python3-template'],
    classifiers=[
        'Development Status :: 3 - Beta',

        'Intended Audience :: Developers :: Research',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: Mozilla Public License 2.0',
    ],
)
