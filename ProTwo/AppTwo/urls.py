from django.urls import path 
from AppTwo import views

urlpatterns = [
    path('', views.help, name='help'),
    path('', views.user, name='user'),
    path('', views.form_name, name='signup'),
]