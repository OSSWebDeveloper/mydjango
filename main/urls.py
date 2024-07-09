from django.urls import path
from . import views
urlpatterns = [
    path('' , views.index , name='index'),
    path('doktor' , views.doktor , name='doktor'),
    path('onas' , views.onas , name='onas'),
    path('xizmat' , views.xizmat , name='xizmat'),
]
