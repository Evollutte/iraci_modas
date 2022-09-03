from django.urls import path
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('galeria/filtro=todos/', views.galeria_todos, name='galeria-todos'),
  path('galeria/filtro=masculino/', views.galeria_masculino, name='galeria-masculino'),
  path('galeria/filtro=feminino/', views.galeria_feminino, name='galeria-feminino'),
  path('galeria/filtro=infantil/', views.galeria_infantil, name='galeria-infantil'),
  path('contato-sobre/', views.contato_sobre, name='contato-sobre'),
  path('sobre-produto/<int:pk>/', views.sobre_produto, name='sobre-produto')
]