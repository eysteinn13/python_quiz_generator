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
    categories_list = []
    for i, c in enumerate(categories):
        response = urlopen(Request("http://jservice.io/api/category" + '?id=' + str(c)))
        resp_parsed = json.loads(response.read().decode())
        categories_list.append(resp_parsed['clues'])
    counter = 0
    questions = []
    answers = []
    for i in range(number_of_questions):
        rand = randint(0, len(categories_list[counter]))
        question = categories_list[counter][rand]['question']
        answer = categories_list[counter][rand]['answer']
        if question == '' or answer == '':
            while question != '' and answer != '':
                rand = randint(0, len(categories_list[counter]))
                question = categories_list[counter][rand]['question']
                answer = categories_list[counter][rand]['answer']
        questions.append((i+1, question))
        answers.append((i+1, answer))
        if counter == len(categories_list) - 1:
            counter = 0
        else :
            counter += 1
    return render(_request, 'quiz_generator/questions.html', {'questions':questions, 'answers':answers})