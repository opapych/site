#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Team Opapy'
SITENAME = u'Opapy - An Professional League of Legends Player'
SITEURL = ''
GITHUB_URL= 'https://github.com/opapy-ch/site'
DISQUS_SITENAME = "opapy-ch"

PATH = 'content'
STATIC_PATHS = [
    'assets',
    'extra/CNAME',
    'extra/favicon.ico',
]
EXTRA_PATH_METADATA = {
    'extra/CNAME': {
        'path': 'CNAME'
    },
    'extra/favicon.ico': {
        'path': 'favicon.ico'
    },
}
USE_FOLDER_AS_CATEGORY = True

TIMEZONE = 'Asia/Tokyo'
DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_LANG = u'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('opapy@op.gg', 'http://na.op.gg/summoner/userName=opapy'),
)

# Social widget
SOCIAL = (
    ('YouTube Gaming', 'https://gaming.youtube.com/channel/UCSMQz1KCumR2LiqwRg0M5Sg'),
)

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
