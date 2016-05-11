from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h2>HEYYOALA</h2>")
def home(request):
    return render(request, 'quiz_generator/home.html')