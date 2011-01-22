# -*- coding: utf-8 -*-
# Django settings for account project

import os.path
import posixpath
import pinax

PINAX_ROOT = os.path.abspath(os.path.dirname(pinax.__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# tells Pinax to use the default theme
PINAX_THEME = "default"

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    # ("Your Name", "your_email@domain.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "adamanderikahines",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}

TIME_ZONE = "US/Eastern"

LANGUAGE_CODE = "en-us"

SITE_ID = 1

USE_I18N = False

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

MEDIA_URL = "/site_media/media/"

STATIC_ROOT = os.path.join(PROJECT_ROOT, "site_media", "static")

STATIC_URL = "/site_media/static/"

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "media"),
    os.path.join(PINAX_ROOT, "media", PINAX_THEME),
]

ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

SECRET_KEY = ")-r%o7%)vh7k@_bi9kf15ai&6jn9gorskp5z4yshr*r^-ann7q"

TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.load_template_source",
    "django.template.loaders.app_directories.load_template_source",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django_openid.consumer.SessionConsumer",
    "django.contrib.flatpages.middleware.FlatpageFallbackMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "pinax.apps.account.middleware.LocaleMiddleware",
    "pinax.middleware.security.HideSensistiveFieldsMiddleware",
    "servee.wysiwyg.middleware.WysiwygMiddleware",
    "servee.toolbar.middleware.ToolbarMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "adamanderikahines.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PINAX_ROOT, "templates", PINAX_THEME),
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
    
    "staticfiles.context_processors.static_url",
    
    "pinax.core.context_processors.pinax_settings",
    
    "pinax.apps.account.context_processors.account",
]

INSTALLED_APPS = [
    # At the Top for pre-loading before contrib.admin
    "admin_tools",
    "admin_tools.theming",
    "admin_tools.menu",
    "admin_tools.dashboard",
    
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.flatpages",
    "django.contrib.humanize",
    "django.contrib.messages",
    "django.contrib.markup",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.webdesign",
    
    "pinax.templatetags",
    
    # external
    "ajax_validation",
    "biblion",
    "debug_toolbar",
    "django_openid",
    "easy_thumbnails",
    "emailconfirmation",
    "idios",
    "improved_inlines",
    "mailer",
    "pagination",
    "south",
    "staticfiles",
    "timezones",
    "treebeard",
    "uni_form",
    
    # sentry
    "sentry",
    "sentry.client",
    "paging",
    "indexer",
    
    # servee
    "servee",
    "servee.wysiwyg",
    "servee.wysiwyg.tinymce",
    "servee.toolbar",

    # media
    "servee.contrib.media.image",
    "servee.contrib.media.video",
    "servee.contrib.media.document",
    "servee.contrib.media.gallery",

    # toolbars
    "servee.contrib.tools.gallery",
    
    # Pinax
    "pinax.apps.account",
    "pinax.apps.signup_codes",
    
    # project
    "profiles",
    "rsvp",
]

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# Account
ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_REQUIRED_EMAIL = False
ACCOUNT_EMAIL_VERIFICATION = False
ACCOUNT_EMAIL_AUTHENTICATION = False
ACCOUNT_UNIQUE_EMAIL = EMAIL_CONFIRMATION_UNIQUE_EMAIL = False

AUTHENTICATION_BACKENDS = [
    "pinax.apps.account.auth_backends.AuthenticationBackend",
]

LOGIN_URL = "/account/login/" # @@@ any way this can be a url name?
LOGIN_REDIRECT_URLNAME = "what_next"

# Biblion
BIBLION_SECTIONS = [
    ("news", "News"),
]

# Idios
ABSOLUTE_URL_OVERRIDES = {
    "auth.user": lambda o: "/profiles/%s/" % o.username,
}
AUTH_PROFILE_MODULE = "profiles.Profile"

# django-email-confirmation
EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG

# Debug Toolbar
DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

# Servee 
SRV_WYSIWYG_EDITOR = "tinymce"

# Django Admin Tools
ADMIN_TOOLS_MENU = "adamanderikahines.menu.CustomMenu"
ADMIN_TOOLS_THEMING_CSS = "css/admin_tools.css"
ADMIN_TOOLS_INDEX_DASHBOARD = "adamanderikahines.dashboard.CustomIndexDashboard"


try:
    from local_settings import *
except ImportError:
    pass
