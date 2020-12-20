#!/usr/bin/env python

from setuptools import setup

setup(
    name='nekogirl',
    version='0.0.2',
    author='mcwindy',
    author_email='chen_yuyang@outlook.com',
    url='https://github.com/mcwindy/nekogirl',
    description='这个代码提供了猫娘',
    packages=['nekogirl'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'Nekogirl=nekogirl:Nekogirl'
        ]
    }
)
