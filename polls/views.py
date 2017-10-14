from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'polls/index.html')

def search(request):
    return render(request, 'polls/search.html')

def voting(request):
    return render(request, 'polls/voting.html')