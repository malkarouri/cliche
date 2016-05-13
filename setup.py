#!/usr/bin/env python

from setuptools import setup, find_packages

PROJECT = 'Pyt'
VERSION = '0.1'


setup(
    name=PROJECT,
    version=VERSION,
    description="A Python skeleton project",

    author="Muhammad Alkarouri",
    author_email="malkarouri@tabahuth.com",

    install_requires=['cliff'],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'pyt = pyt.main:main'
        ],
    },
)
