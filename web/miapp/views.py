from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin 
from .forms import CustomCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
from miapp.models import *

from django.core.paginator import Paginator

# Create your views here.

class Home(LoginRequiredMixin,generic.TemplateView):
    template_name = 'bases/home.html'
    login_url = 'miapp:login'


def registro(request):
    data = {
        'form': CustomCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #redirigir al home
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "te has registrado correctamente")
            return redirect(to="/pagina")
        data["form"] = formulario

    return render(request, 'bases/registro.html', data)

@login_required(login_url='miapp:login')
def pagina(request):

    articles = Article.objects.all()

    return render(request, 'bases/pagina.html', {
        'title': 'Articulos',
        'articles': articles
    })

def category(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category_id)

    return render(request, 'bases/category.html', {
        'category': category,
        'articles': articles
    })

def article(request, article_id):

    article = get_object_or_404(Article, id=article_id)

    return render(request, 'bases/articles.html', {
        'article': article
    })


def nopor(request):
    #sacar articulos
    articles = Article.objects.all()

    #paginar para cada articulo
    paginator = Paginator(articles, 10)

    #recoger numero de pagina
    page = request.GET.get('page')

    page_articles = paginator.get_page(page)

    return render(request, 'bases/nopor.html', {
        'title': 'Articulos',
        'articles': page_articles,
        
    })

    

    #return render(request, 'bases/nopor.html')
