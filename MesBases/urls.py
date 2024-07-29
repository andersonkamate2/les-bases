from django.contrib import admin
from django.urls import path
from blogSimple.views import index, connexion, about, graphique

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', connexion, name='index'),
    path('connexion/', index, name='connexion'),
    path('about/', about, name='a_propos'),
    path('graphique/', graphique, name='graphique'),
]
