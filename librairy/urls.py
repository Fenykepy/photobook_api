from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from librairy import views

urlpatterns = [

    url(r'^picture/$', views.PictureList.as_view(), name="picture-list"),
    url(r'^picture/(?P<sha1>[-\w]+)/$', views.PictureDetail.as_view(), name="picture-detail"),
    
    url(r'^album/$', views.AlbumList.as_view(), name="album-list"),
    url(r'^album/(?P<slug>[-\w]+)/$', views.AlbumDetail.as_view(), name="album-detail"),

    url(r'^tags/$', views.tags_flat_list, name="tags-list"),
    url(r'^$', views.librairy_root, name='librairy-root'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
