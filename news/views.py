from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.conf import settings
from django_comments.forms import CommentForm
from .models import Article, Categoria, Comment
from .forms import UserRegistrationForm, CommentForm
from django.db import models  # Añadir esta línea

def index(request):
    # Lista de slugs para los artículos específicos que quieres mostrar
    specific_slugs = ['islam', 'max', 'celtics', 'connor']
    specific_articles = Article.objects.filter(slug__in=specific_slugs)

    sports_images = {
        'futbol': 'fulbo.jpg',
        'basketball': 'fondonba.jpg',
        'ufc': 'Jirii.jpg',
        'formula1': 'Estasi.jpg',
        'tenis': 'Tennis.jpg'
    }

    context = {
        'specific_articles': specific_articles,
        'sports_images': sports_images
    }

    return render(request, 'news/index.html', context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'news/article_detail.html', {'article': article})

@user_passes_test(lambda u: u.is_superuser)
def delete_article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        article.delete()
        messages.success(request, "El artículo ha sido eliminado exitosamente.")
        return redirect('index')
    else:
        messages.error(request, "No se puede eliminar el artículo de esta manera.")
        return redirect('article_detail', slug=slug)

def about(request):
    return render(request, 'news/about.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'news/register.html', {'form': form})

def login_required_message(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Para leer el artículo debes estar Registrado. Regístrate para no perderte de ninguna noticia!")
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return function(request, *args, **kwargs)
    return wrapper

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página principal
            else:
                messages.error(request, 'Username or password not correct')
                return redirect('login')
        else:
            messages.error(request, 'Invalid login details')
    else:
        form = AuthenticationForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('index')

def category_view(request, category_name):
    return render(request, 'news/category.html', {'category_name': category_name})

def futbol(request):
    articles = Article.objects.filter(categoria__nombre='futbol').order_by('-published_date')
    show_special_article = True  # Puedes configurar esto basado en condiciones específicas si lo deseas
    return render(request, 'news/futbol.html', {
        'articles': articles,
        'show_special_article': show_special_article
    })

def ufc(request):
    articulos = Article.objects.filter(categoria__nombre='UFC')
    return render(request, 'news/ufc.html', {'articulos': articulos})

def basketball(request):
    articulos = Article.objects.filter(categoria__nombre='Basketball')
    return render(request, 'news/basketball.html', {'articulos': articulos})


def formula1(request):
    articulos = Article.objects.filter(categoria__nombre='Formula1')
    return render(request, 'news/formula1.html', {'articulos': articulos})

def tenis(request):
    articulos = Article.objects.filter(categoria__nombre='Tenis')
    return render(request, 'news/tenis.html', {'articulos': articulos})


def show_article(request, article_id):
    article = Article.objects.get(id=article_id)  # Asegúrate de manejar correctamente los casos donde el artículo no exista
    return render(request, 'news/article_template.html', {'article': article})

@login_required_message
def special_article(request):
    return render(request, 'news/special_article.html')

@login_required_message
def winspain(request):
    return render(request, 'news/winspain.html')

@login_required_message
def italywin(request):
    return render(request, 'news/italywin.html')

@login_required_message
def suiza(request):
    return render(request, 'news/suiza.html')

@login_required_message
def argentina(request):
    return render(request, 'news/argentina.html')

@login_required_message
def uruguay(request):
    return render(request, 'news/uruguay.html')


def plantilla_de_grupos(request):
    groups_data = [
        {'group': 'A', 'teams': [
            {'name': 'Argentina', 'PJ': 0, 'G': 0, 'E': 0, 'P': 0, 'DIF': 0, 'PTS': 0},
            {'name': 'Perú', 'PJ': 0, 'G': 0, 'E': 0, 'P': 0, 'DIF': 0, 'PTS': 0},
            # Más equipos...
        ]},
        {'group': 'B', 'teams': [
            {'name': 'México', 'PJ': 0, 'G': 0, 'E': 0, 'P': 0, 'DIF': 0, 'PTS': 0},
            {'name': 'Ecuador', 'PJ': 0, 'G': 0, 'E': 0, 'P': 0, 'DIF': 0, 'PTS': 0},
            # Más equipos...
        ]},
        # Más grupos...
    ]
    context = {'groups': groups_data}
    return render(request, 'plantilla_de_grupos.html', context)


@login_required_message
def nbacampeones(request):
    return render(request, 'news/nbacampeones.html')

@login_required_message
def finalesnba(request):
    return render(request, 'news/finalesnba.html')

@login_required_message
def celtics(request):
    return render(request, 'news/celtics.html')

@login_required_message
def kyrie_luka(request):
    return render(request, 'news/kyrie-luka.html')

@login_required_message
def mavs(request):
    return render(request, 'news/mavs.html')

@login_required_message
def libresnba(request):
    return render(request, 'news/libresnba.html')

@login_required_message
def connor(request):
    return render(request, 'news/connor.html')

@login_required_message
def trecientostres(request):
    return render(request, 'news/trecientostres.html')

@login_required_message
def dominick(request):
    return render(request, 'news/dominick.html')

@login_required_message
def poirier(request):
    return render(request, 'news/poirier.html')

@login_required_message
def islam(request):
    return render(request, 'news/islam.html')

@login_required_message
def makvspoi(request):
    return render(request, 'news/makvspoi.html')

@login_required_message
def pilotos(request):
    return render(request, 'news/pilotos.html')

@login_required_message
def checo(request):
    return render(request, 'news/checo.html')

@login_required_message
def ranking(request):
    return render(request, 'news/ranking.html')

@login_required_message
def max(request):
    return render(request, 'news/max.html')

@login_required_message
def russell(request):
    return render(request, 'news/russell.html')

@login_required_message
def nuevaf1(request):
    return render(request, 'news/nuevaf1.html')

@login_required_message
def sabalenka(request):
    return render(request, 'news/sabalenka.html')

@login_required_message
def murray(request):
    return render(request, 'news/murray.html')

@login_required_message
def sinner(request):
    return render(request, 'news/sinner.html')
    

@login_required_message
def nadal(request):
    return render(request, 'news/nadal.html')

@login_required_message
def djokovic(request):
    return render(request, 'news/djokovic.html')

@login_required_message
def alcaraz(request):
    return render(request, 'news/alcaraz.html')

