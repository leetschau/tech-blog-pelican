#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Li Chao'
SITENAME = 'DarkMatter in Cyberspace'
SITEURL = 'http://leetschau.github.io'

LANDING_PAGE_ABOUT = {'title': 'DarkMatter in Cyberspace',
                      'details': '<p>Welcome to my tech blog.</p>'
        'I am a machine learning engineer in Beijing, China.</br>'
        '<a href="mailto:leetschau@gmail.com">Contact me</a> for any '
        'questions about machine learning algorithms, Python, R and Linux :)'}

PROJECTS = [{
    'name': 'Github Page',
    'url': 'http://github.com/leetschau/',
    'description': 'my gitHub homepage'},
    {'name': 'Stackoverflow Page',
     'url': 'https://stackoverflow.com/users/701420/chad',
     'description': 'my stackoverflow homepage'}]

PATH = 'content'

TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'en'

THEME = '../pelican-themes/elegant'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 40

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'render_math', 'tipue_search']

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives',
                     'search', '404'))

STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

SITEMAP = {
        'format': 'xml'
}
