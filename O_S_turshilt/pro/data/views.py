from django.shortcuts import render
from django.http import HttpResponseRedirect
# from django import forms
from .models import Center, Imformation , Passenger
from django.urls import reverse
# Create your views here.


def index(request):
    # return HttpResponse("sn bnu")
    return render(request, "index.html", {"tr":Imformation.objects.all()})
def a_transport(request, transport_id):
    # return HttpResponse("sn bnu")
    a_trans= Imformation.objects.get(pk=transport_id)
    non_passengers=Passenger.objects.exclude(transports=a_trans).all()
    return render(request, "a_transport.html",{"a_trans": a_trans , "passengers":a_trans.passengers.all() , "non_passengers":non_passengers} )
def book(request, transport_id):
    if request.method=="POST":
        transport= Imformation.objects.get(pk=transport_id)
        passenger_id = int( request.POST["passenger"])
        passenger=Passenger.objects.get(pk=passenger_id)
        passenger.transports.add(transport)
        return HttpResponseRedirect(reverse("a_transport" , args=(transport_id,)))




