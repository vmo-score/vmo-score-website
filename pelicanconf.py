#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jaime Arias, Myriam Desainte-Catherine &amp; Shlomo Dubnov'
SITENAME = u'Interactive Machine Improvisation Scenarios'
SITEURL = ''

THEME = 'theme'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Static Files
STATIC_PATHS = ['blog', 'images', 'examples']
ARTICLE_PATHS = ['blog']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('github', 'https://github.com/vmo-score/vmo-score'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-cite']

PUBLICATIONS_SRC = 'content/files/references.bib'

# Custom Theme parameters
SITELOGO = ''
SITETITLE = 'VMO-Score'
SITESUBTITLE = '''Automatic Construction of Interactive Machine Improvisation
                  Scenarios from Audio Recordings'''
COPYRIGHT_YEAR = 2017
FAVICON = SITEURL + '/theme/img/favicon.ico'
