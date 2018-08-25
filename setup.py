#!/usr/bin/env python

# Copyright (c) 2018 Fabrice Laporte - kray.me
# The MIT License http://www.opensource.org/licenses/mit-license.php

from setuptools import setup


def coerce_file(fn):
    """Coerce .py file content to something useful for setuptools.setup()"""
    import ast, os, re, time  # noqa
    text = open(os.path.join(os.path.dirname(__file__), fn)).read()
    if fn.endswith('.py'):  # extract version, docstring etc out of python file
        mock = type('mock', (object,), {})()
        for attr in ('version', 'author', 'author_email', 'license', 'url'):
            regex = r'^__%s__\s*=\s*[\'"]([^\'"]*)[\'"]$' % attr
            m = re.search(regex, text, re.MULTILINE)
            setattr(mock, attr, m.group(1) if m else None)
        mock.docstring = ast.get_docstring(ast.parse(text))
        if mock.version.endswith('dev'):
            mock.version += str(int(time.time()))
        return mock
    return text


setup(name='memedict',
    version=coerce_file('memedict/__init__.py').version,
    description=coerce_file('memedict/__init__.py').docstring,
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
