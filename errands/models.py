from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    testi = models.CharField(max_length=50, blank=True, null=True)
    img = models.ImageField(upload_to="images")
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Video(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    vid = models.FileField(upload_to="video", null=True)

    def __str__(self):
        return self.name
  