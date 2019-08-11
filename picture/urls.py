from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from picture import views

urlpatterns = [

    url(r'^picture/$', views.PictureList.as_view(), name="picture-list"),
    url(r'^picture/(?P<pk>[0-9]+)/$', views.PictureDetail.as_view(), name="picture-detail"),
    
    url(r'^album/$', views.AlbumList.as_view(), name="album-list"),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetail.as_view(), name="album-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
