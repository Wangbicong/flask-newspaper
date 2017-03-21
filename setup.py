# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='newspaper',
    packages=['newspaper'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-admin',
        'flask-sqlalchemy',
        'flask-restful',
        'mysql-python',
        'requests'
    ],
)
