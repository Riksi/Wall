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
	user = User.objects.filter(id = user_id)
	tiles = Tile.objects.filter(author_id=user_id)
	if user:
		return render(request,'tiles.html',{'tiles':tiles, 'user': user[0]})
	else:
		return HttpResponse('This user does not exist!')

def deleteTile(request,user_id,tile_id):
	user = User.objects.get(id = user_id)
	tile = Tile.objects.get(id=tile_id)
	tile.delete()
	tiles = Tile.objects.all()
	return redirect('myTiles',user_id=user.id)

def editTile(request,user_id,tile_id):
	return HttpResponse('Edit page')

def shareTile(request,user_id,tile_id):
	user = User.objects.get(id = user_id)
	tile = Tile.objects.get(id=tile_id)
	tile.public = 'True'
	tile.save()
	return redirect('myTiles',user_id=user.id)

def unShareTile(request,user_id,tile_id):
	user = User.objects.get(id = user_id)
	tile = Tile.objects.get(id=tile_id)
	tile.public = 'False'
	tile.save()
	return redirect('myTiles',user_id=user.id)

def tileSolved(request,user_id,tile_id):
	user = User.objects.get(id = user_id)
	tile = Tile.objects.get(id=tile_id)
	tile.solved = 'True'
	tile.save()
	return redirect('myTiles',user_id=user.id)

def settings(request,user_id):
	return HttpResponse('Your settings')