from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('articles/<slug:slug>/delete/', views.delete_article, name='delete_article'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('category/<str:category_name>/', views.category_view, name='category_view'),
    path('futbol/', views.futbol, name='futbol'),
    path('basketball/', views.basketball, name='basketball'),
    path('ufc/', views.ufc, name='ufc'),
    path('formula1/', views.formula1, name='formula1'),
    path('tenis/', views.tenis, name='tenis'),
    path('special-article/', views.special_article, name='special_article'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('winspain/', views.winspain, name='winspain'),
    path('italywin/', views.italywin, name='italywin'),
    path('suiza/', views.suiza, name='suiza'),
    path('argentina/', views.argentina, name='argentina'),
    path('uruguay/', views.uruguay, name='uruguay'),
    path('nbacampeones/', views.nbacampeones, name='nbacampeones'),
    path('finalesnba/', views.finalesnba, name='finalesnba'),
    path('plantilla_de_grupos/', views.plantilla_de_grupos, name='plantilla_de_grupos'),
    path('celtics/', views.celtics, name='celtics'),
    path('kyrie-luka/', views.kyrie_luka, name='kyrie-luka'),
    path('mavs/', views.mavs, name='mavs'),
    path('libresnba/', views.libresnba, name='libresnba'),
    path('connor/', views.connor, name='connor'),
    path('trecientostres/', views.trecientostres, name='trecientostres'),
    path('dominick/', views.dominick, name='dominick'),
    path('poirier/', views.poirier, name='poirier'),
    path('islam/', views.islam, name='islam'),
    path('makvspoi/', views.makvspoi, name='makvspoi'),
    path('pilotos/', views.pilotos, name='pilotos'),
    path('checo/', views.checo, name='checo'),
    path('ranking/', views.ranking, name='ranking'),
    path('max/', views.max, name='max'),
    path('russell/', views.russell, name='russell'),
    path('nuevaf1/', views.nuevaf1, name='nuevaf1'),
    path('sabalenka/', views.sabalenka, name='sabalenka'),
    path('murray/', views.murray, name='murray'),
    path('sinner/', views.sinner, name='sinner'),
    path('nadal/', views.nadal, name='nadal'),
    path('djokovic/', views.djokovic, name='djokovic'),
    path('alcaraz/', views.alcaraz, name='alcaraz'),
]
