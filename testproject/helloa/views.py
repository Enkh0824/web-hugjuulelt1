from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# Create your views here.


class NewTestForm(forms.Form):
        test=forms.CharField(label='юм бичих')
        password = forms.CharField(max_length=32, widget=forms.PasswordInput)

def test(request):
    # return HttpResponse("sn bnu")
    return render(request, "helloa/test.html", {"form":NewTestForm()})

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
    
    

