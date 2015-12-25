from django.shortcuts import render
from django.http import HttpResponse

user = {'username': 'Anush', 'score':-1}

tiles = [{'id': 1, 'created': 'today', 'content': 'I am very sad'},
		{'id': 2, 'created': 'today',  'content': 'Why do I not manage to do things properly?'},
		{'id': 3, 'created': 'today', 'content': 'Why do I not have anything to show?'},
		{'id': 4, 'created': 'today',  'content': 'I really want to accomplish things but seem to lack motivation'},
]

# Create your views here.
def welcome(request):
	return render(request,'welcome.html',{})

def myTiles(request,user_id):
	return render(request,'tiles.html',{'tiles':tiles, 'user': user})

def settings(request,user_id):
	return HttpResponse('Your settings')