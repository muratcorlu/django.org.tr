from django.conf.urls.defaults import *


urlpatterns = patterns('websites.views',
    url(r'^$', 'website_list', name='website_list'),
    
)
