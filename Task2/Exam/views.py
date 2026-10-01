from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testPaper(reuqest):
    s = "<h1>Q1: Who developed the Python programming language?</h1> <br> <h3>A) Dennis Ritchie</h3> <br> <h3>B) James Gosling</h3> <br> <h3> C) Guido van Rossum</h3> <br> <h3>D) Bjarne Stroustrup</h3>"
    return HttpResponse(s)

def result(request):
    s = "<h1> Pass</h1>"
    return HttpResponse(s)  