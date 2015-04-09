from django.conf.urls import include, url
from django.contrib import admin
from parse import urls as parse_urls


urlpatterns = [
    # Examples:
    # url(r'^$', 'mediaplayground.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include(parse_urls))
]
