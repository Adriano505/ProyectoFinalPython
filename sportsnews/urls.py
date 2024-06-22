from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('comments/', include('django_comments.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]