from django.conf.urls import include, url
from . import api, views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'posts', api.PostViewSet)

urlpatterns = [
    # url(r'^posts/$', api.post_list),
    url(r'^', include(router.urls)),

    url(r'^$', views.post_list),
    url(r'^new/$', views.post_new),
    url(r'^sum/(?P<numbers>[0-9/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]{2,4})/(?P<age>\d{1,3})/$', views.hello),
]

