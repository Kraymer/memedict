#!/usr/bin/env python

# Copyright (c) 2018 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

from setuptools import setup


__version__ = '1.0.1'

setup(name='memedict',
    version=__version__ if not __version__.endswith('dev') else __version__ + str(int(time.time()),
    description='Knowyourmeme.com definitions scraper',
    long_description=coerce_file('README.md'),
    author='Fabrice Laporte',
    author_email='kraymer@gmail.com',
    url='https://github.com/KraYmer/memedict',
    license='MIT',
    platforms='ALL',

    packages=[
      'memedict',
    ],
    install_requires=coerce_file('requirements.txt').split('\n'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Communications :: Chat',
    ],
    keywords="Know Your Meme desciptions web scraper.",
    )
