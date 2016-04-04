"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from article.views import detail, test, home, archives, about, tag, search, RSSFeed

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', test),
    # url(r'^id/([0-9])+/', database, name='database'),
    url(r'^([0-9]+)', detail, name='detail'),
    url(r'^id/(?P<id>\d+)/$', detail, name='detail'),
    url(r'^$', home),
    url(r'^archives/$', archives),
    url(r'^about/$', about),
    url(r'^tag/(?P<tag>\w+)/$', tag, name='tag'),
    url(r'^search/$', search, name='search'),
    url(r'^feed/$', RSSFeed(), name="RSS"),

]
