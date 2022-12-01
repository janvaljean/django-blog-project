from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def index():
    return HttpResponse("home page")

def blogs():
    return HttpResponse("blogs")


def blog_details():
    return HttpResponse("blog detzauils")
