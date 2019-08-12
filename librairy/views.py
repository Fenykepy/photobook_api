from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from librairy.serializers import *
from librairy.models import Picture, Tag, Album


@api_view(('GET', ))
@permission_classes([AllowAny])
def librairy_root(request, format=None):
    return Response({
        'picture-list': reverse('picture-list', request=request, format=format),
        'album-list': reverse('album-list', request=request, format=format),
        'tags-list': reverse('tags-list', request=request, format=format),
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
        queryset = Picture.objects.filter(user=user)
        tag = self.request.query_params.get('tag', None)
        if tag is not None:
            tag = get_object_or_404(Tag, name=tag)
            queryset = queryset.filter(tag=tag)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class PictureDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This view presents a specific picture and allows to update
    or delete it.
    """
    serializer_class = PictureSerializer
    queryset = Picture.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Picture.objects.filter(user=user)



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

    def get_queryset(self):
        user = self.request.user
        return Album.objects.filter(user=user)


@api_view(['GET'])
def tags_flat_list(request, format=None):
    """
    Returns a flat list of all tags without pagination.
    """
    tags = Tag.objects.order_by('name').values_list('name',
            flat=True)

    return Response(tags)
