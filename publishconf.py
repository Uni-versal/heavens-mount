#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://heavensmount.com'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

AUTHOR = 'Arc'
SITENAME = "Heaven's Mount" 
SITEURL = '/' 
PATH = 'content' 
TIMEZONE = 'Europe/London' 
DEFAULT_LANG = 'en' 
FEED_ALL_ATOM = None 
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None 
AUTHOR_FEED_ATOM = None 
AUTHOR_FEED_RSS = None
GOOGLE_ANALYTICS_ID = None
GOOGLE_ANALYTICS_PROP = None 
# Blogroll
LINKS = (('Home', SITEURL), ('Arc', 'https://twitter.com/rainlife__'), ) 
SOCIAL = ()
DEFAULT_PAGINATION = False 
#RELATIVE_URLS = True 
THEME = './themes/voce/'
PLUGIN_PATHS = ['./themes/voce/plugins/'] 
PLUGINS = ['assets'] 
MANGLE_EMAILS = True
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DEFAULT_CATEGORY = 'Misc'
