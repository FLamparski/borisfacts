from django.conf.urls import url, include

from . import views

app_name = 'yourstories'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^stories/$', views.index, name='index'),
    url(r'^stories/post/$', views.post, name='post'),
    url(r'^stories/post/handler/$', views.post_handler, name='post_handler'),
    url(r'^stories/(?P<id>[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})/$', views.story, name='story'),
    url(r'^stories/(?P<id>[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})/verify/(?P<code>[0-9A-Fa-f]{8}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{4}-[0-9A-Fa-f]{12})/$', views.verify, name='verify')
]
