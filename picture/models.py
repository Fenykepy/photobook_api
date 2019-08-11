from django.db import models
from django.contrib.auth.models import User

class Picture(models.Model):
    """Table for all pictures."""
    sha1 = models.CharField(max_length=42, db_index=True)
    source_file = models.ImageField()
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
        #TODO parse tags here
        super(Picture, self).save()



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
