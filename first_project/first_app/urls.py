from django.conf.urls import url
from first_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.kitty, name='kitty' ),
    url(r'^$', views.form_name_view, name='form'),
]