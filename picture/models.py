import os
import hashlib
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User



class PictureFileSystemStorage(FileSystemStorage):
    """FileSystemStorage which does nothing if name exists."""
    def get_available_name(self, name, max_length=None):
        return name

    def _save(self, name, content):
        if self.exists(name):
            # file exists, we do not call the superclasses _save method
            return name
        # file is new, we call superclasses _save method
        return super(PictureFileSystemStorage, self)._save(name, content)



def get_sha1_hexdigest(file):
    """
    Return sha1 hexadecimal sum of given file.
    """
    sha1 = hashlib.sha1()
    for chunk in file.chunks():
        sha1.update(chunk)

    return sha1.hexdigest()



def set_pathname(instance, filename):
    """
    Set pathname this way:
    pictures/full/4a/52/4a523fe9c50a2f0b1dd677ae33ea0ec6e4a4b2a9
    """
    return os.path.join(
            'pictures',
            'full',
            instance.sha1[0:2],
            instance.sha1[2:4],
            instance.sha1
    )



class Picture(models.Model):
    """Table for all pictures."""
    sha1 = models.CharField(max_length=42, db_index=True)
    source_file = models.ImageField(
            upload_to=set_pathname,
            storage=PictureFileSystemStorage()
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,
            verbose_name="Creation date")
    date_updated = models.DateTimeField(auto_now=True,
            verbose_name="Last modification date")
    description = models.TextField(verbose_name="Picture description")

    class Meta:
        ordering = ['date_created']
        indexes = [
            models.Index(fields=['sha1', 'user'])
        ]
        unique_together = ['sha1', 'user']

    
    def save(self, **kwargs):
        # compute sha1 here
        self.sha1 = get_sha1_hexdigest(self.source_file)
        super(Picture, self).save()
        
        # parse and add tags here
        hashtags = extract_hashtags(self.description)
        print(hashtags)
        for hashtag in hashtags:
            tag, created = Tag.objects.get_or_create(name=hashtag)
            tag.pictures.add(self)



class Tag(models.Model):
    """Table for all tags."""
    name = models.CharField(primary_key=True, max_length=254)
    pictures = models.ManyToManyField(Picture, blank=True)



class Album(models.Model):
    """Table for all albums."""
    name = models.CharField(db_index=True, max_length=254)
    description = models.TextField(blank=True, verbose_name="Album description")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True,
            verbose_name="Creation date")
    date_updated = models.DateTimeField(auto_now=True,
            verbose_name="Last modification date")
    pictures = models.ManyToManyField(Picture, blank=True)



def extract_hashtags(s):
    return set(part[1:] for part in s.split() if part.startswith('#'))
