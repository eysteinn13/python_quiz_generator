from django.conf.urls import url
from django.views.generic import ListView, DetailView
from quiz_generator.models import Question
from . import views

urlpatterns = [
    url(r'^home', ListView.as_view(queryset=Question.objects.all().order_by("question_ID")[:25],
                                    template_name="quiz_generator/tester.html")),
    url(r'^', views.home, name='home')
]