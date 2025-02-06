from django.urls import  path

from User import views

urlpatterns = [
    path('get_token/',views.get_user_role_and_tg_id,name='get_user_role_and_tg_id'),
]