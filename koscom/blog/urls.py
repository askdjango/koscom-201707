from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^new/$', views.post_new),
    url(r'^sum/(?P<numbers>[0-9/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]{2,4})/(?P<age>\d{1,3})/$', views.hello),
]

