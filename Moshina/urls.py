from django.urls import path
from .views import *

urlpatterns = [
    path('b/', index1),
    path('i/', index2),
    path('r/', index3),
    path('u/', index4),
    path('s/', index5),
]