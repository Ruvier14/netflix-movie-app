from django.db import models


# We create our own models here
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to="videos/", null=True, blank=True)

    def __str__(self):
        return self.title