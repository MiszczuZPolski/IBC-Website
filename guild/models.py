from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_images', blank=True)

    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return self.title

    def get_likes_count(self):
        return self.likes.count()
