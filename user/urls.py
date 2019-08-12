from django.conf.urls import url
from user.views import user_root


urlpatterns = [
    url(r'^$', user_root, name='user-root'),
]
