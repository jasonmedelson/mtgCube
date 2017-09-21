from django.conf.urls import url
from . import views #get current dir views

urlpatterns = [
    #/cards/
    url(r'^$', views.index, name='index')


]