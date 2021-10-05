#!/usr/bin/env python3

from setuptools import setup

setup(
    name='kellerLD',
    version='0.0.1',
    description='kellerLD driver',
    author='Blue Robotics',
    url='https://github.com/bluerobotics/kellerLD-python',
    packages=['kellerLD'],
    package_data={ "kellerLD": ["kellerLD.meta"]},
    entry_points={
        'console_scripts': [
            'kellerld-report=kellerLD.report:main',
            'kellerld-test=kellerLD.test:main',
        ],
    },
    install_requires=['smbus'],
)
