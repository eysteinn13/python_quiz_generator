from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen, Request
import json
from random import randint
# Create your views here.

def getReq(_request):
    req = Request("http://jservice.io/api/clues")
    response = urlopen(req)
    resp_parsed = json.loads(response.read().decode())
    questions_answers = []
    for resp in resp_parsed:
        tup = (resp['question'], resp['answer'])
        questions_answers.append(tup)
    return render(_request, 'quiz_generator/home.html', {'questions':questions_answers})


def getCategory(_request, categoryID):
    categories = _request.POST.getlist('check')
    response = urlopen(Request("http://jservice.io/api/category" + '?id=' + str(categoryID)))
    resp_parsed = json.loads(response.read().decode())
    clues = resp_parsed['clues']
    question_answers = []
    for c in clues:
        tup = (c['question'], c['answer'])
        question_answers.append(tup)
    return render(_request, 'quiz_generator/home.html', {'questions':question_answers})


# TODO make only one API call for each category
def getQuiz(_request):
    categories = _request.POST.getlist('check[]')
    number_of_questions = int(_request.POST.get('spinner'))
    counter = 0
    questions = []
    for i in range(number_of_questions):
        response = urlopen(Request("http://jservice.io/api/category" + '?id=' + str(categories[counter])))
        resp_parsed = json.loads(response.read().decode())
        clues = resp_parsed['clues']
        rand = randint(0,len(clues))
        tup = (clues[rand]['question'], clues[rand]['answer'])
        questions.append(tup)
        if counter == len(categories) - 1:
            counter = 0
        else :
            counter += 1
    return render(_request, 'quiz_generator/questions.html', {'questions':questions})