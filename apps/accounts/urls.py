from django.urls import path
from . import views


urlpatterns = [
  path('perfil/', views.Perfil.as_view(), name='perfil'),
  path('perfil-atualiza/<int:pk>/', views.Perfil_atualiza.as_view(), name='perfil-atualiza'),
  path('perfil-excluir/<int:pk>/', views.Perfil_excluir.as_view(), name='perfil-excluir'),
  path('favoritos/', views.favoritos, name='favoritos'),
  path('sobre-produto-favorito/<int:pk>', views.sobre_produto_favorito, name='sp-favorito'),
]
