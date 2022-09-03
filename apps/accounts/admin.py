from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserChangeForm, UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
  form = UserChangeForm
  add_form = UserCreationForm
  model = User
  list_display = ['username', 'first_name', 'email', 'cpf', 'telephone', 'genre']
  search_fields = ['username', 'first_name', 'email', 'cpf', 'telephone', 'genre']
  fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Mais informações', {'fields': (
          'genre',
          'birth_date', 
          'cpf', 
          'address',
          'telephone',
          'zip_code',
          'district'
          )}),
    )
