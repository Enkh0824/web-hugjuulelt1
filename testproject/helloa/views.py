from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    # return HttpResponse("sn bnu")
    return render(request, "helloa/index.html", {"value": "sain baina uu" , "type":"mongol", "a":78, "items":["hjkl","ghjkl;","ertye"]})
def wrong(request):
    return HttpResponse ("buruu site")
def uidalt(request):
    return HttpResponse ("yu bnda")

def greeting(request,language):
    if "mongolian" in language: 
        return HttpResponse("amar bnu")
    elif "chinise" in language:
        return HttpResponse("ni hao")
    elif "russian" in language:
        return HttpResponse("snovi gdom")
    else: 
        return HttpResponse("hello")

