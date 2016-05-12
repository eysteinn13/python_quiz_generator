from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen, Request
import json
# Create your views here.

def home(request):
    return render(request, 'quiz_generator/home.html')

def home(request):
    return render(request, 'quiz_generator/home.html', {'content':['If you bblablabla', 'Another text woohoo']})

def getReq(_request):
    print('LALALALALLAALLALA')
    req = Request("http://jservice.io/api/clues")
    response = urlopen(req)
    resp_parsed = json.loads(response.read().decode())
    questions_answers = []
    for resp in resp_parsed:
        tup = (resp['question'], resp['answer'])
        questions_answers.append(tup)
    return render(_request, 'quiz_generator/home.html', {'questions':questions_answers})


def getCategory(_request, categoryID):
    print(categoryID)
    request_url = "http://jservice.io/api/category" + '?id=' + str(categoryID)
    print(request_url)
    req = Request(request_url)
    response = urlopen(req)
    resp_parsed = json.loads(response.read().decode())
    questions_answers = []
    for resp in resp_parsed:
        tup = (resp['question'], resp['answer'])
        questions_answers.append(tup)
    print(questions_answers)
    return render(_request, 'quiz_generator/home.html', {'questions': questions_answers})