# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from configparser import ConfigParser

def get_config(path='package_info.ini'):
    cp = ConfigParser()
    cp.read('package_info.ini')
    config = cp['package']
    return config

def get_version(path='version'):
    version = ""
    with open('version', 'r') as f:
        version = f.read().strip()
    return version

def get_requirements(path='requirements'):
    reqs = []
    try:
        with open('requirements.txt', 'r') as f:
            reqs =  f.read().split()
        return reqs
    except Exception:
        return []

config = get_config(path='package_info.ini')

setup(
    name                = config["name"],
    version             = get_version(path='version'),
    description         = 'logstash logger module',
    author              = config["author"],
    author_email        = config["author_email"],
    url                 = config["url"],
    install_requires    = get_requirements(path='requirements.txt'),
    packages            = find_packages(exclude = ['venv', 'tests']),
    keywords            = ['logstash', 'python', 'logger'],
    python_requires     = '>=3',
)