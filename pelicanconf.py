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
LINKS = (('Home', SITEURL),
         ('Arc', 'https://twitter.com/rainlife__'),
         )

SOCIAL = ()

DEFAULT_PAGINATION = False
#RELATIVE_URLS = True

THEME = './themes/voce/'

PLUGIN_PATHS = ['./themes/voce/plugins/']
PLUGINS = ['assets']

USER_LOGO_URL = '/images/header_logo.png'
MANGLE_EMAILS = True

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DEFAULT_CATEGORY = 'Misc'
