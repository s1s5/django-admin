"""admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import re
from typing import List, Union
from urllib.parse import urlparse

from django.conf import settings
from django.contrib import admin
from django.urls import URLPattern, URLResolver, path, re_path

from . import views

urlpatterns: List[Union[URLResolver, URLPattern]] = [
    path(settings.ADMIN_URL_PREFIX, admin.site.urls),
]

if settings.ADMIN_INDEX_TITLE:
    admin.site.index_title = settings.ADMIN_INDEX_TITLE

if settings.ADMIN_SITE_TITLE:
    admin.site.site_title = settings.ADMIN_SITE_TITLE

if settings.ADMIN_SITE_HEADER:
    admin.site.site_header = settings.ADMIN_SITE_HEADER

if not settings.DEBUG:
    urlpatterns.insert(
        0,
        re_path(
            r"^%s(?P<path>.*)$" % re.escape(urlparse(settings.STATIC_URL).path.lstrip("/")),
            views.serve_static_files,
        ),
    )
