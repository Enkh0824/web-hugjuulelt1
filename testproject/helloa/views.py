from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("sn bnu")
def wrong(request):
    return HttpResponse ("buruu site")
def uidalt(request):
    return HttpResponse ("yu bnda")
def greeting(request,language):
    if "mongolian" in language
    return HttpResponse("amar bnu")
    elif "chinise" in language:
        return HttpResponse("ni hao")
    elif "russian" in language:
        return HttpResponse(snovi gdom)
    else: 
        return HttpResponse("hello")
urlpatterns = [
    ... 
    path("str:language>",views.greeting,name="greeting"),
    ... 
]
