from django.conf.urls import url
from user.views import user_root
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    url(r'^token/$', TokenObtainPairView.as_view(), name="token-obtain"),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name="token-refresh"),
    url(r'^$', user_root, name='user-root'),
]
