from django.urls import path
from .import views
urlpatterns = [
    path ("",views.index,name="index"),
    path ("w",views.wrong,name="wrong"),
    path ("u",views.uidalt,name="uidalt")
]