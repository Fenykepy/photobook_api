from django.contrib.auth import login

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.views import LoginView as KnoxLoginView


@api_view(('GET', ))
@permission_classes([AllowAny])
def user_root(request, format=None):
    return Response({
        'login': reverse('knox-login', request=request, format=format),
        'logout': reverse('knox-logout', request=request, format=format),
    })




class LoginView(KnoxLoginView):
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        serializer=AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)




