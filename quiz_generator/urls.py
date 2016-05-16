from django.conf.urls import url
from django.views.generic import ListView, DetailView
from . import views

urlpatterns = [
    url(r'^$', views.getReq, name='getReq'),
    url(r'^home/$', views.getReq, name='getReq'),
    url(r'^home/(?P<categoryID>\d+)$', views.getCategory),
    url(r'^home/questions$', views.getQuiz),
    url(r'^home/questions/answers', views.postAnswers),
    url(r'^home/questions/pdf', views.getPDF)
]
