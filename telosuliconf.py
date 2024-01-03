#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# PELICAN VARIABLES REFERENCED BY TEMPLATE

OWNER = ""
AUTHOR = ""

SITENAME = ""

SOURCE_CODE_URL = ""

USER_LOGO_URL = ""
TAGLINE = ""

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

LINK_ITEMS = (
    # ("<LABEL>", "<LINK_TEXT>", "<URL>"),
)
SOCIAL = ()

# CONFIGURATIONS FOR PELICAN BUILD PROCESS

THEME = "telosuli"

# PLUGINS

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = [
    #"autopages",
    #"similar_posts",
    "neighbors",
    #"more_categories",
    "photos",
    "summary",
    "pelican.plugins.read_more",
]

# autopages
AUTOPAGES_PATH = ""

AUTHOR_PAGE_PATH = ""
CATEGORY_PAGE_PATH = ""
TAG_PAGE_PATH = ""

# similar_posts
SIMILAR_POSTS_MAX_COUNT = 3

# photos
PHOTO_LIBRARY = ""

PHOTO_SQUARE_THUMB = True
PHOTO_RESIZE_JOBS = 5
PHOTO_WATERMARK = False

PHOTO_EXIF_KEEP = False
PHOTO_EXIF_REMOVE_GPS = True

PHOTO_EXIF_COPYRIGHT = "CC-BY-SA"
PHOTO_EXIF_COPYRIGHT_AUTHOR = ""

# summary
SUMMARY_USE_FIRST_PARAGRAPH = True

# scripts
# GOATCOUNTER_URL = 'https://rwev.goatcounter.com/count'
GOATCOUNTER_URL = ''

# CONFIGURATIONS FOR TELOSULI STATIC APPEARANCE (NOT USED BY PELICAN)

TELOSULI_SEPARATION_STR = " // "

TELOSULI_SOCIAL = "social"

TELOSULI_HOME = "home"

TELOSULI_BLOG = "blog"
TELOSULI_PAGES = "pages"
TELOSULI_LINKS = "links"

TELOSULI_ARCHIVES = "archives"
TELOSULI_SIMILAR_ARTICLES = "similar articles"

TELOSULI_AUTHOR = "author"
TELOSULI_AUTHORS = "authors"
TELOSULI_AUTHOR_S = "author(s)"

TELOSULI_CATEGORY = "category"
TELOSULI_CATEGORIES = "categories"

TELOSULI_ARTICLES = "articles"

TELOSULI_GALLERY = "gallery"

TELOSULI_TAG = "tag"
TELOSULI_TAGS = "tags"

TELOSULI_PREVIOUS = "prev"
TELOSULI_NEXT = "next"

TELOSULI_NEWER = "newer"
TELOSULI_OLDER = "older"

TELOSULI_POSTED = "posted"
TELOSULI_MODIFIED = "modified"

TELOSULI_ATOM = "atom"
TELOSULI_RSS = "rss"

THEME_URL = "https://github.com/oldherl/telosuli"

# FORMATTING / FEED GENERATION

DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M"  # big

TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None

AUTHOR_FEED_ATOM = "feeds/author.{slug}.atom.xml"
AUTHOR_FEED_RSS = "feeds/author.{slug}.rss.xml"

TAG_FEED_ATOM = "feeds/tag.{slug}.atom.xml"
TAG_FEED_RSS = "feeds/tag.{slug}.rss.xml"

CATEGORY_FEED_ATOM = "feeds/category.{slug}.atom.xml"
CATEGORY_FEED_RSS = "feeds/category.{slug}.rss.xml"

DISPLAY_SUB_FEEDS = False # whether to display author, tag, and category feeds

FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS =  "feeds/all.rss.xml"
