from django.urls import  path

from User import views

urlpatterns = [
    path('', views.user, name='home'),
]