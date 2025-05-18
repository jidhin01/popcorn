from django.db import models

# Create your models here.
class moviet(models.Model):
    movie_name=models.CharField(max_length=50)
    movie_year=models.CharField(max_length=50)
    movie_duration=models.CharField(max_length=50)
    movie_description=models.CharField(max_length=500)
    movie_image=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.movie_name
