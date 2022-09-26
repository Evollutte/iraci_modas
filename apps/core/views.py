from itertools import product
from unicodedata import category
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.core.mail import send_mail
from apps.product.models import Product
from apps.banner.models import Banner
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def paginators(request, objects, amount):

  paginator = Paginator(objects, amount)

  # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
  try:
    page = int(request.GET.get('page', '1')) 
  except ValueError:
    page = 1

  # Se o page request (9999) está fora da lista, mostre a última página.
  try:
    objects = paginator.page(page)
  except (EmptyPage, InvalidPage):
    objects = paginator.page(paginator.num_pages)
  
  return objects
  

def home(request):
  product = Product.objects.all() #[:8] Quantidade itens que vai ser mostrado
  product = paginators(request, product, 3) # Mostra 8 produtos por página
  banner = Banner.objects.all()
  return render(request, 'core/index.html', {'product':product, 'banner':banner})


def galeria_todos(request):
  product = Product.objects.all()
  product = paginators(request, product, 8) # Mostra 8 produtos por página
  return render(request, 'core/galeria.html', {'product':product})


def galeria_masculino(request):
  product = Product.objects.filter(category='Masculino')
  product = paginators(request, product, 8) # Mostra 8 produtos por página
  return render(request, 'core/galeria.html', {'product':product})


def galeria_feminino(request):
  product = Product.objects.filter(category='Feminino')
  product = paginators(request, product, 8) # Mostra 8 produtos por página
  return render(request, 'core/galeria.html', {'product':product})


def galeria_infantil(request):
  product = Product.objects.filter(category='Infantil')
  product = paginators(request, product, 8) # Mostra 8 produtos por página
  return render(request, 'core/galeria.html', {'product':product})


def contato_sobre(request):
  dice = {}
  if request.method == 'POST':
    dice['nome'] = request.POST.get('nome')
    dice['email'] = request.POST.get('email')
    dice['telefone'] = request.POST.get('telefone')
    # dice['tipo'] = request.POST.get('tipo')
    dice['mensagem'] = request.POST.get('mensagem')

    send_mail(
      dice['nome'],
      'Remetente: ' + dice['email'] + '\n\n' + 'Telefone: ' + dice['telefone'] + '\n\n' + 'Mensagem: ' + dice['mensagem'],
      '',
      [settings.EMAIL_HOST_USER],
      # [settings.EMAIL_BACKEND],
    )
    return redirect('/')
  return render(request, 'core/contato.html', dice)


def sobre_produto(request, pk):
  product = get_object_or_404(Product, pk=pk)

  if request.method == 'POST':
    if not product.favorite.filter(id=request.user.id).exists():
      product.favorite.add(request.user)

      return redirect('favoritos')

  return render(request, 'core/sobre_produto.html', {'product':product})


def view_404(request, exception):
  product = Product.objects.all()[:8] # Quantidade itens que vai ser mostrado
  product = paginators(request, product, 8) # Mostra 8 produtos por página
  return render(request, 'core/index.html', {'product':product})
