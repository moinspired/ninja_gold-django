from django.shortcuts import render, HttpResponse, redirect
from random import randint
import datetime, os
def index(request):
    return render(request,'golds/index.html')

def summary(request):
    now = datetime.datetime.now()
    # del request.session["gold"]
    # try:
    #     del request.session["earned"]
    # except:
    #     print "caugth error"
    if "gold" in request.session:
        if request.POST["form_id"] == "1015": #Value referance for Gold 
            value = randint(10, 20)
            request.session["gold"] += value
            request.session["earned"].append("Earned " + str(value) + " golds from the farm! " + now.strftime("%Y-%m-%d %H:%M"))
        elif request.POST["form_id"] == "1016": #form id referance for Cave 
            value = randint(5, 10)
            request.session["gold"] += value
            request.session["earned"].append("Earned " + str(value) + " golds from the cave! " + now.strftime("%Y-%m-%d %H:%M"))
        elif request.POST["form_id"] == "1017": #form id referance for House
            value = randint(2, 5)
            request.session["gold"] += value
            request.session["earned"].append("Earned " + str(value) + " golds from the house! " + now.strftime("%Y-%m-%d %H:%M"))
        elif request.POST["form_id"] == "1018": #form id referance for Casino
            value = randint(-50, 50)
            if value > 0:
                request.session["gold"] += value
                request.session["earned"].append("Earned " + str(value) + " golds from the casino! " + now.strftime("%Y-%m-%d %H:%M"))
            else:
                request.session["gold"] += value
                request.session["lost"].append("Entered a casino and lost " + str(value) + "golds...Ouch. " + now.strftime("%Y-%m-%d %H:%M"))
    else: 
        request.session["gold"] = 0
        request.session["earned"] = []
        request.session["lost"] = []
        
    return redirect('/')