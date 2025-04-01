from django.shortcuts import render
from django.http import HttpResponse
from django import forms
# Create your views here.


class NewTestForm(forms.Form):
        test=forms.CharField(label='юм бичих')
        password = forms.CharField(max_length=32, widget=forms.PasswordInput)

def index(request):
    # return HttpResponse("sn bnu")
    return render(request, "index.html", {"form":NewTestForm()})





