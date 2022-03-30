from django.urls import path
from . import views

#URL conf model
urlpatterns = [
    path('hello/', views.say_hello)
]