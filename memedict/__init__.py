#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Knowyourmeme.com definitions scraper.
"""

import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher


SEARCH_SIMILARITY_THRESHOLD = .4

HEADERS = {'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')}


def search_meme(text):
    """Return a meme name and url from a meme keywords.
    """
    r = requests.get('http://knowyourmeme.com/search?q=%s' % text, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    memes_list = soup.find(class_='entry_list')
    if memes_list:
        meme_paths = [meme['href'] for meme in memes_list.find_all('a', href=True)]
        meme_names = [meme_path.replace('-', ' ') for meme_path in meme_paths]
        meme_urls = ['https://knowyourmeme.com%s' % meme_path for meme_path in meme_paths]
        return zip(meme_names, meme_urls)
    return [(None, None)]


def search(text):
    """Return a meme definition from a meme keywords.
    """
    meme_names_and_urls = search_meme(text)
    sequence_match_ratios = [SequenceMatcher(None, text, meme_name_and_url[0]).ratio()
                             for meme_name_and_url in meme_names_and_urls]
    best_match = meme_names_and_urls[sequence_matches.index(max(sequence_matches))]
    meme_name, url = best_match[0], best_match[1]

    if meme_name and SequenceMatcher(None, text, meme_name).ratio() >= SEARCH_SIMILARITY_THRESHOLD:
        r = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        entry = soup.find('h2', {'id': 'about'})
        return '%s. %s' % (meme_name.split('/')[-1].title(), entry.next.next.next.text)
