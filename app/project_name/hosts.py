from . import admin_urls
from django_hosts import patterns, host

host_patterns = patterns(
  '',
    host(r'admin', admin_urls, name='admin'),
    host(r'', 'home.urls', name=' '),
)
