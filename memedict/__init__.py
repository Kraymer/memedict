#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Knowyourmeme.com definitions scraper.
"""

import requests
from bs4 import BeautifulSoup

__author__ = 'Fabrice Laporte <kraymer@gmail.com>'
__version__ = '0.1.0-dev'


HEADERS = {'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')}


def search_meme(text):
    """Return a meme url from a meme keywords.
    """
    r = requests.get('http://knowyourmeme.com/search?q=%s' % 'base belong to us', headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    memes_list = soup.find(class_='entry_list')
    meme_path = memes_list.find('a', href=True)['href']
    return 'https://knowyourmeme.com%s' % meme_path


def search(text):
    """Return a meme definition from a meme keywords.
    """
    r = requests.get(search_meme(text), headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    return(soup.find('h2').next.next.next.text)
