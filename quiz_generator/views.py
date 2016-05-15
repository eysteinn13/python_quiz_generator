from django.shortcuts import render
from django.http import HttpResponse
from urllib.request import urlopen, Request
import json
from random import randint
import pdfkit


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
    if len(categories) == 0 or number_of_questions == 0:
        return render(_request, 'quiz_generator/home.html')

    categories_list = []
    for i, c in enumerate(categories):
        response = urlopen(Request("http://jservice.io/api/category" + '?id=' + str(c)))
        resp_parsed = json.loads(response.read().decode())
        categories_list.append(resp_parsed['clues'])
    counter = 0
    questions = []
    answers = []
    both = []
    for i in range(number_of_questions):
        rand = randint(0, len(categories_list[counter]) - 1)
        question = categories_list[counter][rand]['question']
        answer = categories_list[counter][rand]['answer']
        if question == '' or answer == '' or isQuestionInList(question, questions):
            while isQuestionInList(question, questions) or question == '' or answer == '':
                rand = randint(0, len(categories_list[counter]))
                question = categories_list[counter][rand]['question']
                answer = categories_list[counter][rand]['answer']
        (q, a) = check(question, answer)
        question = q
        answer = a
        questions.append((i+1, question, categories_list[counter][rand]['category_id']))
        answers.append((i+1, answer))
        both.append((i+1, question, answer))
        if counter == len(categories_list) - 1:
            counter = 0
        else :
            counter += 1


    # laga þetta - er bara að breyta skránni beint ekki django -> html -> pdf
    # pdfkit.from_file('/Users/valarun/Documents/HR/Vor 2016/python/verk5 - part2/saumaklubbur/quiz_generator/templates/quiz_generator/questions.html', 'quiz.pdf')

    return render(_request, 'quiz_generator/questions.html', {'questions':questions, 'answers':answers, 'both': both})

def postAnswers(_request):
    answers = _request.POST.getlist('answer[]')
    right_answers = _request.POST.getlist('right_answer[]')
    cleaned_answers = []
    for i in answers:
        j = i.replace(' ', '')

    print(answers)
    return render(_request, 'quiz_generator/answers.html', {'answers': answers})

def getPDF(_request):
    questions = _request.POST.getlist('pdf_questions[]')
    answers = _request.POST.getlist('pdf_answers[]')
    print(questions)
    print(answers)
    return render(_request, 'quiz_generator/pdf.html', {'questions': questions, 'answers':answers})


def isQuestionInList(question, list):
    for tuple in list:
        if question == tuple[1]:
            return True
    return False

def check(q, a):
    if '\\' in q:
        q = q.replace('\\', '')
    if '\\' in a:
        a = a.replace('\\', '')
    if '<i>' in q:
        q = q.replace('<i>', '')
    if '<i>' in a:
        a = a.replace('<i>', '')
    if '</i>' in a:
        a = a.replace('</i>', '')
    if '</i>' in q:
        q = q.replace('</i>', '')

    return (q, a)


