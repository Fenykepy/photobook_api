from django.conf.urls import url
from knox import views as knox_views
from user.views import LoginView, user_root


urlpatterns = [
    url(r'login/', LoginView.as_view(), name='knox-login'),
    url(r'logout/', knox_views.LogoutView.as_view(), name='knox-logout'),
    url(r'^$', user_root, name='user-root'),
]
