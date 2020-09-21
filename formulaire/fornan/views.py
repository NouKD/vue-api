from django.shortcuts import render
from. import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# Create your views here.

def index(request):
    
    datas = {

    }

    return render(request, 'index.html', datas)

def exo2(request):
    
    datas = {

    }

    return render(request, 'exo2.html', datas)    

def exo(request):
    
    datas = {

    }

    return render(request,'exo.html', datas)

def pdata(request):

    if request.method == 'POST':
        json_data = json.loads(request.body)
        print(json_data)
        print(json_data['nom'])
        print(json_data['prenom'])

    datas = {
        'satus': True
    }

    return JsonResponse(datas, safe = False)


def podata(request):
    message = ""
    status = False
    if request.method == 'POST':
        json_data = json.loads(request.body)
        # print(json_data)
        # print(json_data['nom'])
        # print(json_data['prenom'])
        # print(json_data['age'])
        # print(json_data['email'])
        # print(json_data['genre'])
        # print(json_data['phone'])

        nom = json_data['nom']
        prenom = json_data['prenom']
        age = json_data['age']
        email = json_data['email']
        phone = json_data['phone']
        genre = json_data['genre']
        # status=False

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

@csrf_exempt
def postdata(request):
    status = False
    message = "api"

    if request.method == 'POST':
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        date = request.POST.get('date')
        genre = request.POST.get('genre')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        try:
            print('ici')
            exist = models.Customer.objects.filter(email=email)[:1].get()
            status = False
            message = " l'adresse email exist deja"
        except:
            try:
                if nom != '' and prenom != '' and date != '' and genre != '' and email !='' and phone != '' :

                    us = models.Customer(
                            nom= nom,
                            prenom= prenom,
                            date= date,
                            genre= genre,
                            email= email,
                            phone= phone,
                        )

                    us.save()

                    message = 'votre candidature a bien ete enregistre'

            except models.Customer.DoesNotExist:
                
                message = "remplicez bien tous les champs"

    else:
        status = False
        message = "erreur de l'enregistrement"

    print(message)
    datas={
        'status': status,
        'message': message
    }

    return JsonResponse(datas, safe=False)