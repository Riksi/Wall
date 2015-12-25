from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.welcome,name='welcome'),
				url(r'^(?P<user_id>[0-9]+)/tiles$', views.myTiles,name='myTiles'), 
				url(r'^(?P<user_id>[0-9]+)/settings$', views.settings,name='settings'),
				url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/delete$', views.deleteTile,name='delete'),
				url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/edit$', views.editTile,name='edit'),
				url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/share$', views.shareTile,name='share'),
				url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/solved$', views.tileSolved,name='solved')]