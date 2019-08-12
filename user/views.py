from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny



@api_view(('GET', ))
@permission_classes([AllowAny])
def user_root(request, format=None):
    return Response({''
    })





