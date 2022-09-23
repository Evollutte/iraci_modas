from email.headerregistry import Address
from django.db import models
from django.contrib.auth.models import AbstractUser

from .validate import validate_CPF


GENRE = (
  ('Masculino', 'Masculino'),
  ('Feminino', 'Feminino'),
  ('Outro', 'Outro'),
)


class User(AbstractUser):
  genre = models.CharField(max_length=9, choices=GENRE, verbose_name='Gênero')
  birth_date = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
  cpf = models.CharField(max_length=14, verbose_name='CPF', validators=[validate_CPF])
  address = models.CharField(max_length=120, verbose_name='Endereço')
  telephone = models.CharField(max_length=20, verbose_name='Telefone')
  zip_code = models.CharField(max_length=20, verbose_name='CEP')
  district = models.CharField(max_length=120, verbose_name='Bairro')

  def __str__(self):
    return self.username
