#!/usr/bin/env python

# Copyright (c) 2018 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

import os
import time

from setuptools import setup

VERSION = '1.0.3'
DIRPATH = os.path.dirname(__file__)

setup(name='memedict',
    version=VERSION if not VERSION.endswith('dev') else '%s%s' % (VERSION, int(time.time())),
    description='Knowyourmeme.com definitions scraper',
    long_description=open(os.path.join(DIRPATH, 'README.md')).read(),
    author='Fabrice Laporte',
    author_email='kraymer@gmail.com',
    url='https://github.com/KraYmer/memedict',
    license='MIT',
    platforms='ALL',

    packages=[
      'memedict',
    ],
    install_requires=open(os.path.join(DIRPATH, 'requirements.txt')).read().split('\n'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
    ],
    keywords="Know Your Meme desciptions web scraper.",
    )
