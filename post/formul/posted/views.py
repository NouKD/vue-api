from django.shortcuts import render
from. import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

def index(request):
    
    datas = {

    }

    return render(request, 'index.html', datas)


def postdata(request):
    message = ""
    status = False
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)

            nom = json_data['nom']
            prenom = json_data['prenom']
            age = json_data['age']
            email = json_data['email']
            phone = json_data['phone']
            genre = json_data['genre'] 
        except :
            nom = request.POST.get('nom')
            prenom = request.POST.get('prenom')
            age = request.POST.get('age')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            genre = request.POST.get('genre')  

        try:
            if nom != '' and prenom != '' and age != '' and genre != '' and email !='' and phone != '' :
                us = models.User(
                        nom= nom,
                        prenom= prenom,
                        age= age,
                        genre= genre,
                        email= email,
                        phone= phone,
                    )
 
                us.save()
                status = True
                message = 'votre candidature a bien ete enregistre'
            else:
                status = False
                message = "remplicez bien tous les champs"
        except models.User.DoesNotExist:
            status = False
            message = "Une erreur ses Produite"
    else:
        status = False
        message = "erreur de requête"

    datas = {
        'status': status,
        'message' : message,
    }

    return JsonResponse(datas, safe = False)