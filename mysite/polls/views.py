from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(requset):
	return HttpResponse("Hello, world. You're at the polls index.")