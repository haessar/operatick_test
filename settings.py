"""
Django settings for operatick project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from decouple import config
from melodramatick.settings import *  # noqa: F401, F403
from melodramatick.settings import INSTALLED_APPS as IMPORTED_APPS
from melodramatick.settings import (
    BASE_DIR, ALLOWED_HOSTS, TEMPLATES, STATICFILES_DIRS
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS.extend(["vm", "127.0.0.1", "operatick"])

#  Application definition

INSTALLED_APPS = ['operatick'] + IMPORTED_APPS + ['django_extensions']

# ROOT_URLCONF = 'melodramatick.urls'

TEMPLATES[0]['DIRS'].extend([BASE_DIR / "operatick" / "templates"])


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# if DEVELOPMENT_MODE is True:
#     DATABASES['default']['NAME'] = BASE_DIR / 'db.sqlite3'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_DIRS = [BASE_DIR / "operatick" / "static"] + STATICFILES_DIRS

# APIs

GOOGLE_CLOUD_SERVICE_ACCOUNT_JSON = BASE_DIR / config('GOOGLE_CLOUD_SERVICE_ACCOUNT_JSON', default='')


# Site-specific settings

WORK_MODEL = 'operatick.Opera'
WORK_PLURAL_LABEL = 'operas'

SITE = 'Operatick'
BACKGROUND_COLOUR = "#ecdff2"

LANGUAGE_CHOICES = sorted(
    [
        ("it", "Italian"),
        ("en", "English"),
        ("de", "German"),
        ("ru", "Russian"),
        ("cz", "Czech"),
        ("fr", "French"),
        ("la", "Latin"),
        ("sa", "Sanskrit"),
        ("hu", "Hungarian"),
        ("es", "Spanish"),
        ("po", "Polish"),
        ("da", "Danish"),
        ("fi", "Finnish"),
        ("sv", "Swedish"),
        ("lt", "Lithuanian"),
        ("hy", "Armenian"),
        ("nl", "Dutch"),
        ("fa", "Persian"),
    ],
    key=lambda x: x[1]
)

SITE_ID = 1

GRAPH_MODELS = {
    # 'all_applications': True,
    'app_labels': ["composer", "opera", 'performance', 'listen', 'top_list', "accounts"],
    'group_models': False,
}
