from django.contrib import admin
from django.urls import path
from blogSimple.views import index, connexion, about, graphique

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connexion/', connexion, name='index'),
    path('about/', index, name='connexion'),
    path('', about, name='a_propos'),
    path('graphique/', graphique, name='graphique'),
]
