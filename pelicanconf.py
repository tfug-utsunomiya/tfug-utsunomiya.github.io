#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'tfug-utsunomiya'
SITENAME = 'TFUG Utsunomiya Blog'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('TensorFlow', 'https://www.tensorflow.org/'),
         ('TFUG Utsunomiya', 'https://tfug-utsunomiya.connpass.com/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/tfug-utsunomiya'),
          ('Twitter', 'https://twitter.com/search?q=%23tfug_utsunomiya'),
          ('Facebook', 'https://www.facebook.com/groups/762136920622347'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'extra/favicon.ico'
]
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}