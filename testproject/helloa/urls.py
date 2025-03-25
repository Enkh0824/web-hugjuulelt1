from django.urls import path
from .import views
urlpatterns = [
    # path ("",views.index,name="index"),
    path ("w",views.wrong,name="wrong"),
    path ("u",views.uidalt,name="uidalt"),
    # path("<str:language>",views.greeting,name="greeting"),
    path ("test",views.test,name="test"),

]