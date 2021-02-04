# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name                = 'logstash-logger',
    version             = '1.0.0.1',
    description         = 'logstash logger module',
    author              = 'segulee',
    author_email        = 'segulee@gmail.com',
    url                 = 'https://github.com/segulee/logstash_logger',
    download_url        = 'https://github.com/segulee/logstash_logger/archive/1.0.0.1.tar.gz',
    install_requires    = [
        "python-logstash==0.4.6"
    ],
    packages            = find_packages(exclude = ['venv']),
    keywords            = ['logstash', 'python', 'logger'],
    python_requires     = '>=3',
)