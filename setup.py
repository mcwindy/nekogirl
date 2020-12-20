#!/usr/bin/env python

from setuptools import setup

setup(
    name='nekogirl',
    version='0.0.3',
    license='WTFPL',
    description='An open source python package used to import nekogirl.',
    author='mcwindy',
    author_email='chen_yuyang@outlook.com',
    url='https://github.com/mcwindy/nekogirl',
    packages=['nekogirl'],
    install_requires=[
        "random"
    ],
    entry_points={
        'console_scripts': [
            'Nekogirl=nekogirl:Nekogirl'
        ]
    }
)
