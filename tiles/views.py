from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from .forms import TileForm, RegForm
from .models import Tile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse


user = {'id': 2, 'username': 'Anush', 'score':-1}

tiles = [{'id': 1, 'created': 'today', 'content': 'I am very sad'},
		{'id': 2, 'created': 'today',  'content': 'Why do I not manage to do things properly?'},
		{'id': 3, 'created': 'today', 'content': 'Why do I not have anything to show?'},
		{'id': 4, 'created': 'today',  'content': 'I really want to accomplish things but seem to lack motivation'},]

# Create your views here.


def test(request):
	return render(request,'tiles/test.html',{})

def myTiles(request,user_id):
	if request.method == "POST":
		form = TileForm(request.POST)
		if form.is_valid():
			tile = form.save(commit=False)
			tile.author = User.objects.get(id = user_id)
			tile.save()
		return redirect('myTiles',user_id=user_id)
	else:
		form = TileForm()
		user = User.objects.filter(id = user_id)
		tiles = Tile.objects.filter(author_id=user_id)
		if user:
			print(request.user.id == user[0].id)
			if request.user.is_authenticated() and request.user.id == user[0].id:
				return render(request,'tiles/tiles.html',{'tiles':tiles, 
												'user': user[0],
												 'form': form})
			else:
				return redirect('%s?next=%s' % (reverse('wallLogin'), request.path))
		else:
			return HttpResponse('This user does not exist!')

def deleteTile(request,user_id,tile_id):

	if request.method == "POST":
		user = User.objects.get(id = user_id)
		tile = Tile.objects.get(id=tile_id)
		tile.delete()
		return redirect('myTiles',user_id=user.id)

	else:
		return render(request,'tiles/tile_delete.html',{})

def editTile(request,user_id,tile_id):
	tile = Tile.objects.get(id=tile_id)
	
	if request.method == "POST":
		form = TileForm(request.POST,instance = tile)
		if form.is_valid():
			tile = form.save(commit=False)
			tile.author = User.objects.get(id = user_id)
			tile.created_date = timezone.now()
			tile.save()
			return redirect('myTiles', user_id=user_id)
		#return redirect('editTile',user_id = user_id, tile_id= tile_id)
		return render(request,'tiles/tile_edit.html',{'form':form})
	else:
		form = TileForm(instance = tile)
		return render(request,'tiles/tile_edit.html',{'form':form})

def shareTile(request,user_id,tile_id):
	user = User.objects.get(id = user_id)
	tile = Tile.objects.get(id=tile_id)
	tile.public = True
	tile.save()
	return redirect('myTiles',user_id=user.id)

def unShareTile(request,user_id,tile_id):
	user = User.objects.get(id = user_id)
	tile = Tile.objects.get(id=tile_id)
	tile.public = False
	tile.save()
	return redirect('myTiles',user_id=user.id)

def tileSolved(request,user_id,tile_id):
	user = User.objects.get(id = user_id)
	tile = Tile.objects.get(id=tile_id)
	tile.solved = True
	tile.save()
	return redirect('myTiles',user_id=user.id)

from django.http import JsonResponse
import random
def ajaxTest(request):
    random_no = random.randint(1,100)
    return JsonResponse({'random_no': random_no})

def settings(request,user_id):
	return HttpResponse('Your settings')



"""def login(request):
	form = RegForm()
	if request.method == "POST":
		
		username = request.POST['username']
		password = request.POST['password']
		print (username)
		#username = form.username
		#password = form.password
		user = authenticate(username=username, password=password)
		print (user)
		if user is not None:
			
			if user.is_active:
				login(request, user)
				return redirect('myTiles',user_id=user.id)
		return render(request,'tiles/welcome.html',{'form': form})

	else:
		form = RegForm()
		return render(request,'tiles/welcome.html',{'form': form})"""

def welcome(request):
	if request.method == "POST":

		form = RegForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			u = User.objects.create_user(username = username, password = password)

			return redirect('myTiles',user_id=u.id)
		"""	
		user = authenticate(username=username, password=password)
		print (user)
		if user is not None:
			
			if user.is_active:
				login(request, user)
				return redirect('myTiles',user_id=user.id)
		"""
		return render(request,'tiles/welcome.html',{'form': form})

	else:
		print(request.user.is_authenticated())
		form = RegForm()
		return render(request,'tiles/welcome.html',{'form': form})

def wallLogin(request):
	if request.method == "POST":
		form = RegForm()
		username = request.POST['uname']
		password = request.POST['pword']
		next = request.POST['next']
		user = authenticate(username=username, password=password)
		
		if user is not None:
			print('Successfully authenticated\n')
			if user.is_active:
				
				login(request, user)

				if next:
					return redirect(next)
				else:
					return redirect(reverse('myTiles', kwargs = {'user_id':user.id}))
		return render(request,'tiles/login.html',{'error' :'You have not correctly entered your username and/or password', 'next':next})
	else:
		next = ''
		if 'next' in request.GET:

			next = next.join(request.GET['next'])
		return render(request,'tiles/login.html', {'error': '','next': next})
#request.get_full_path()

def wallLogout(request):
	logout(request)
	return redirect('welcome')
	
