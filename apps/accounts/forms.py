from allauth.account.forms import SignupForm
from django import forms as as_forms
from django.contrib.auth import forms

from .models import User, GENRE
from .validate import validate_CPF


class UserChangeForm(forms.UserChangeForm):
  class Meta(forms.UserChangeForm.Meta):
    model = User


class UserCreationForm(forms.UserCreationForm):
  class Meta(forms.UserCreationForm.Meta):
    model = User


class MyCustomSignupForm(SignupForm):
  first_name = as_forms.CharField(label='Primeiro Nome')
  last_name = as_forms.CharField(label='Sobrenome')
  genre = as_forms.CharField(label='Gênero')
  birth_date = as_forms.CharField(label='Data de Nascimento')
  cpf = as_forms.CharField(label='CPF', validators=[validate_CPF])
  address = as_forms.CharField(label="Endereço")
  telephone = as_forms.CharField(label='Telefone')
  zip_code = as_forms.CharField(label="CEP")
  district = as_forms.CharField(label="Bairro")

  def __init__(self, *args, **kwargs):
    super(MyCustomSignupForm, self).__init__(*args, **kwargs)
    self.fields['first_name'].widget = as_forms.TextInput(attrs={'placeholder': 'Primeiro Nome'})
    self.fields['last_name'].widget = as_forms.TextInput(attrs={'placeholder': 'Sobrenome'})
    self.fields['genre'].widget = as_forms.RadioSelect(attrs={'placeholder': 'Gênero'}, choices=GENRE)
    self.fields['birth_date'].widget = as_forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'Data de Nascimento', 'type': 'date'})
    self.fields['cpf'].widget = as_forms.TextInput(attrs={'placeholder': 'CPF'})
    self.fields['address'].widget = as_forms.TextInput(attrs={'placeholder': 'Endereço'})
    self.fields['telephone'].widget = as_forms.TextInput(attrs={'placeholder': 'Telefone'})
    self.fields['zip_code'].widget = as_forms.TextInput(attrs={'placeholder': 'CEP'})
    self.fields['district'].widget = as_forms.TextInput(attrs={'placeholder': 'Bairro'})

  def save(self, request):
    user = super(MyCustomSignupForm, self).save(request)
    user.first_name = self.cleaned_data['first_name']
    user.username = user.username.capitalize()
    user.last_name = self.cleaned_data['last_name']
    user.genre = self.cleaned_data['genre']
    user.birth_date = self.cleaned_data['birth_date']
    user.cpf = self.cleaned_data['cpf']
    user.address = self.cleaned_data['address']
    user.telephone = self.cleaned_data['telephone']
    user.zip_code = self.cleaned_data['zip_code']
    user.district = self.cleaned_data['district']
    user.save()
    return user
