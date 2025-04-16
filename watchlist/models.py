from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    watched = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='movie_posters/', null=True, blank=True)

    def __str__(self):
        return self.title