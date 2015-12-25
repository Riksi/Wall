from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import User, Tile

user = {'id': 2, 'username': 'Anush', 'score':-1}

tiles = [{'id': 1, 'created': 'today', 'content': 'I am very sad'},
		{'id': 2, 'created': 'today',  'content': 'Why do I not manage to do things properly?'},
		{'id': 3, 'created': 'today', 'content': 'Why do I not have anything to show?'},
		{'id': 4, 'created': 'today',  'content': 'I really want to accomplish things but seem to lack motivation'},
]

# Create your views here.
def welcome(request):
	return render(request,'welcome.html',{})

def myTiles(request,user_id):
	tiles = Tile.objects.all()
	return render(request,'tiles.html',{'tiles':tiles, 'user': user})

def deleteTile(request,user_id,tile_id):
	tile = Tile.objects.get(id=tile_id)
	tile.delete()
	tiles = Tile.objects.all()
	return redirect('myTiles',user_id=user['id'])

def editTile(request,user_id,tile_id):
	return HttpResponse('Edit page')

def shareTile(request,user_id,tile_id):
	return HttpResponse('Share page')

def tileSolved(request,user_id,tile_id):
	return HttpResponse('Solved page')


def settings(request,user_id):
	return HttpResponse('Your settings')