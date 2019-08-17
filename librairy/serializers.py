from rest_framework import serializers

from librairy.models import Picture, Tag, Album


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
    url = serializers.HyperlinkedIdentityField(
            view_name='album-detail',
            lookup_field='slug',
    )
    pictures = serializers.SlugRelatedField(
        many=True,
        slug_field='sha1',
        read_only=True,
    )
    class Meta:
        model = Album
        fields = ('url', 'title', 'slug', 'description', 'pictures', 'user')
        read_only_fields = ('user', 'slug')



