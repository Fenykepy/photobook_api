from rest_framework import serializers

from picture.models import Picture, Tag, Album


class PictureSerializer(serializers.ModelSerializer):
    """
    A serializer with all pictures data.
    """
    class Meta:
        model = Picture
        fields = (
            'url', 'id', 'sha1', 'source_file', 'user', 'description'
        )
        read_only_fields = ('sha1', 'user')


class TagSerializer(serializers.ModelSerializer):
    """
    A serializer with all tags data.
    """
    class Meta:
        model = Tag
        fields = (
            'name'
        )


class AlbumSerializer(serializers.ModelSerializer):
    """
    A serializer with all albums data.
    """
    class Meta:
        model = Album
        fields = ('name', 'description', 'pictures')



