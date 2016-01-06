from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [url(r'^$', views.Tiles,name='Tiles'),
    # url(
    #     '^login/',
    #     auth_views.login,
    #     {'template_name': 'tiles/login.html',
    #     'redirect_field_name' : '/'r'^(?P<user_id>[0-9]+)/tiles$'
    #     }
    # ),
				#url(r'^$', views.myTiles,name='myTiles'), 
				url(r'^login/$', views.wallLogin,name='wallLogin'), 
				url(r'^logout/$', views.wallLogout,name='wallLogout'),
				url(r'^tiles/settings$', views.settings,name='settings'),
				url(r'^tiles/delete$', views.deleteTile,name='delete'),
				url(r'^tiles/edit$', views.editTile,name='edit'),
				url(r'^(?P<username>[\w\.\+\-\_\@]+)$', views.publicTiles,name='public'),
				#url(r'^(?P<user_id>[0-9 A-z]+)/(?P<tile_id>[0-9]+)/share$', views.shareTile,name='share'),
				#url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/unshare$', views.unShareTile,name='unshare'),
				url(r'^tiles/status$', views.setTileStatus,name='status'),
				url(r'^ajaxtest$', views.ajaxTest,name='ajaxtest'),
				url(r'^test$', views.test,name='test')]