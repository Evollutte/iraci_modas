from unicodedata import category
from django.db import models

from apps.accounts.models import User


CATEGORY = (
  ('Masculino', 'Masculino'),
  ('Feminino', 'Feminino'),
  ('Infantil', 'Infantil'),  
)

SIZE = (
  ('P', 'P'),
  ('M', 'M'),
  ('G', 'G'),
  ('P M', 'P M'),
  ('P G', 'P G'),
  ('M G', 'M G'),
  ('P M G', 'P M G'),
)


class Product(models.Model):
  name = models.CharField(max_length=120, verbose_name='Nome do Produto', unique=True)
  category = models.CharField(max_length=9, choices=CATEGORY, verbose_name='Categoria')
  size = models.CharField(max_length=5, choices=SIZE, verbose_name='Tamanho')
  description = models.TextField(verbose_name='Descrição')
  amount = models.DecimalField(max_digits=100, decimal_places=0, verbose_name='Quantidade')
  price = models.DecimalField(max_digits=100, decimal_places=0, verbose_name='Preço')
  # image_url = models.URLField(max_length=1024, blank=True, null=True)
  image = models.ImageField(upload_to='product/')
  favorite = models.ManyToManyField(User, blank=True, related_name='favorite', verbose_name='Favorito')

  def __str__(self):
    return self.name
