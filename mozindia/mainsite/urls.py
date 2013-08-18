# -.- encoding: utf8 -.-
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from .helpers.download_buttons import download_firefox

from . import views


urlpatterns = patterns('',
    url(r'^$', direct_to_template,
        {
            'template': 'mainsite/home.html',
            'extra_context': {
                'languages': (
                    ('hi-IN',u'हिंदी', u'मुफ्त डाउनलोड करें'),
                    ('en-US', 'English (US)', 'Free Download'),
                ),
            },
        },
        name='mainsite.home'),
)
