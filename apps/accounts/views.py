from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import fields

from apps.product.models import Product
from .models import User


class Perfil(LoginRequiredMixin, ListView):
  login_url = reverse_lazy('account_login')
  model = User
  template_name = 'accounts/perfil.html'

  def get_queryset(self):
    self.object_list = User.objects.filter(first_name=self.request.user)
    return self.object_list


class Perfil_atualiza(LoginRequiredMixin, UpdateView):
  login_url = reverse_lazy('account_login')
  model = User
  fields = ['address', 'telephone', 'zip_code', 'district']
  template_name = 'accounts/perfil_atualiza.html'
  success_url = reverse_lazy('perfil')

  def get_object(self, queryset=None):
    self.object = get_object_or_404(User, pk=self.kwargs['pk'], first_name=self.request.user)
    return self.object


class Perfil_excluir(LoginRequiredMixin, DeleteView):
  login_url = reverse_lazy('account_login')
  model = User
  template_name = 'accounts/perfil_excluir.html'
  success_url = reverse_lazy('perfil')

  def get_object(self, queryset=None):
    self.object = get_object_or_404(User, pk=self.kwargs['pk'], first_name=self.request.user)
    return self.object


@login_required
def favoritos(request):
  user = request.user
  product = user.favorite.all()
  return render(request, 'accounts/favoritos.html', {'product':product})

@login_required
def sobre_produto_favorito(request, pk):
  product = get_object_or_404(Product, pk=pk)
  
  if request.method == 'POST':
    if product.favorite.filter(id=request.user.id).exists():
      product.favorite.remove(request.user)

      return redirect('favoritos')
      
  return render(request, 'accounts/sobre_produto_favorito.html', {'product':product})
