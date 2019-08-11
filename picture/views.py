from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from picture.serializers import *
from picture.models import Picture, Tag, Album


@api_view(('GET', ))
@permission_classes([AllowAny])
def picture_root(request, format=None):
    return Response({
        'picture-list': reverse('picture-list', request=request, format=format),
        'album-list': reverse('album-list', request=request, format=format),
    })


class PictureList(generics.ListCreateAPIView):
    """
    This view presents a list of all pictures and allows
    new pictures to be created.
    """
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Picture.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view presents a specific picture and allows to update
    or delete it.
    """
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()



class AlbumList(generics.ListCreateAPIView):
    """
    This view presents a list of all albums and allows
    new albums to be created.
    """
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    lookup_field = 'slug'

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view presents a specific album and allows to update
    or delete it.
    """
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    lookup_field = 'slug'

