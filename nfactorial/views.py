from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, nfactorial school!")

def add_numbers(request, first, second):
    sum = first + second
    return HttpResponse(str(sum))

def transform(request, word):
    word = word.upper()
    return HttpResponse(word)

def check(request, word):
    if word == word[::-1]:
        return HttpResponse("True")
    else:
        return HttpResponse("False")

def calc(request, first, operation, second):
    if operation == "add":
        return HttpResponse(str(first + second))
    elif operation == "sub":
        return HttpResponse(str(first - second))
    elif operation == "mult":
        return HttpResponse(str(first * second))
    elif operation == "div":
        return HttpResponse(str(first / second))

