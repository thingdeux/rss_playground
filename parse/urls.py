from django.conf.urls import include, url
from django.contrib import admin
from parse.views import display_metadata

urlpatterns = [
    # Examples:
    # url(r'^$', 'mediaplayground.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'parse.views.display_metadata', name='index'),
]