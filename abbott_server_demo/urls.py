"""abbott_server_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from core_file.views import *
from django.conf.urls import include

from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pdf_dir/(?P<file_name>[^/]+)', pdf_dir),
    url(r'^demo_url/', demo_url),
    url(r'^multiple_files/', include("core_file.urls",
        namespace="multiple_files", app_name="multiple_files")),
]
