from django.urls import path
from web import views
from .views import addUser, index
urlpatterns = [
    path('add/', addUser),
    path('', index)
]
