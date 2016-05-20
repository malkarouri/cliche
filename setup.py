#!/usr/bin/env python

from setuptools import setup, find_packages

PROJECT = 'Cliche'
VERSION = '0.1'


setup(
    name=PROJECT,
    version=VERSION,
    description="A Python CLI Framework",

    author="Muhammad Alkarouri",
    author_email="malkarouri@tabahuth.com",

    install_requires=['cliff', 'keyring'],
    namespace_packages=[],
    packages=find_packages(),
    include_package_data=True,

    entry_points={
        'console_scripts': [
            'cliche = cliche.main:main'
        ],
        'mgmt.main': [
            'setenv = cliche.general:SetEnv',
            'getenv = cliche.general:GetEnv',
            'config = cliche.config:Config',
            'keyring = cliche.config:KeyRing',
        ],
    },
)
