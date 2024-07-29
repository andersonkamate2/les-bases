from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
import pyttsx4 as ptt
import datetime
from .models import Etudiant
from django.views.decorators.csrf import csrf_exempt
import math
# Create your views here.
def index(request):

    #Pour changer de voix
    voix = ptt.init()
    """
    voices = voix.getProperty('voices')
    voix.setProperty('voice', voices[1].id)



    #pour changer de volume
    volume = voix.getProperty('volume')
    voix.setProperty('volume', 1)

    #pour changer le debit de parole
    rate = voix.getProperty('rate')
    voix.setProperty('rate', 200)
    """



    calcul = math.sqrt(100)
    cal = math.sqrt(625)
    somme = ("la somme de " + str(calcul) + " + " + str(cal) + " = " + str(cal + calcul))



    #CREATION INTERACTION AVEC LA BASE DE DONNE
    etudiants = Etudiant.objects.all()


    #CREATION VOIX
    sauti =  voix.say("INTERNET CONNEXION, EFFECTUées avec succès.")
    voix.runAndWait()

    return render(request,'blog/index.html',
                  context={'message': 'Hello world',
                   'voix': '',
                   'sauti2':somme,
                   'etudiants': etudiants,
                   'voix': sauti
                  })

User = get_user_model()

def connexion(request):

    heure = datetime.datetime.now()
    if request.method == "POST":
        #traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username,
                                        password=password)
        login(request, user)
        return redirect('connexion')

    return render(request, 'blog/connexion.html', context={'heure':heure})


def about(request):
    voix = ptt.init()
    sauti = voix.say("A propos de nous")
    voix.runAndWait()


    return render(request, 'blog/about.html',context={'voix':sauti,})

def graphique(request):

    #pourfaire le graphique
    import plotly.offline as opy
    import plotly.graph_objs as go

    #creation de donnee
    Annee_2022=[3,10,104, 80, 3]
    Annee_2023=[500,100,299, 500, 10]

    #creation graphique
    trace = go.Scatter(x=Annee_2022, y=Annee_2023)
    data=[trace]
    layout = go.Layout(title="MOn Graphique")
    figure = go.Figure(data=data, layout=layout)

    fig = opy.plot(figure, auto_open=False, output_type='div')


    voix = ptt.init()
    sauti = voix.say("Graphique, activer")
    voix.runAndWait()

    return render(request, 'blog/graphique.html', context={'sauti': sauti,
                                                           'fig':fig})