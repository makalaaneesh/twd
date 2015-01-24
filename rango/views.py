from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	context={'boldmessage': "I am bold"}
	return render(request, 'rango/index.html', context)
	# return HttpResponse("Welcome to the world of rango. Rango says hello world!<br> Learn more <a href='/rango/about'>here</a>")

def about(request):
	# return HttpResponse("This is the about page<br><a href='/rango'>Go back</a>")
	context={}
	return render(request, 'rango/about.html', context)