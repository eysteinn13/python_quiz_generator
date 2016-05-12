from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    url(r'^home/$', views.getReq, name='getReq'),
    url(r'^home/(?P<categoryID>\d+)$', views.getCategory),
    url(r'^home/questions', views.getQuiz)
]
