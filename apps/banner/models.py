from django.db import models


class Banner(models.Model):
  name = models.CharField(max_length=120, verbose_name='Nome', unique=True)
  image_url = models.URLField(max_length=1024, blank=True, null=True)
  image = models.ImageField(upload_to='banner/')

  def __str__(self):
    return self.name