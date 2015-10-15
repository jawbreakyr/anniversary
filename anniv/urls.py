from django.conf.urls import patterns, url

from anniv.views import AnniversaryView

urlpatterns = patterns('',
                       url(r'^$', AnniversaryView.as_view(), name='home'),
                       )
