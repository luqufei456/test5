from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^myexp$', views.myExp),
    url(r'^uploadPic$', views.uploadPic),
    url(r'^uploadHandle$', views.uploadHandle),
    url(r'^userlist/(\d*)$', views.userlist),
    url(r'^area/$', views.area),
    url(r'^area/(\d+)/$', views.area2),
]