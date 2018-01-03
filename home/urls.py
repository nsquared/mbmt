from django.conf.urls import url

from . import views


urlpatterns = [

    # Main website pages.
    url(r'^$', views.index, name='index'),
    url(r'^rules/$', views.rules, name='rules'),
    url(r'^info/$', views.info, name='info'),
    url(r'^about/$', views.about, name='about'),
    url(r'^archive/$', views.archive, name='archive'),
    url(r'^topics/$', views.topics, name='topics'),

]
