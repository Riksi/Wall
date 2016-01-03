from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [url(r'^$', views.welcome,name='welcome'),
    # url(
    #     '^login/',
    #     auth_views.login,
    #     {'template_name': 'tiles/login.html',
    #     'redirect_field_name' : '/'r'^(?P<user_id>[0-9]+)/tiles$'
    #     }
    # ),
				url(r'^(?P<user_id>[0-9]+)/tiles$', views.myTiles,name='myTiles'), 
				url(r'^login/$', views.wallLogin,name='wallLogin'), 
				url(r'^logout/$', views.wallLogout,name='wallLogout'),
				url(r'^(?P<user_id>[0-9]+)/settings$', views.settings,name='settings'),
				url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/delete$', views.deleteTile,name='delete'),
				url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/edit$', views.editTile,name='edit'),
				url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/share$', views.shareTile,name='share'),
				url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/unshare$', views.unShareTile,name='unshare'),
				url(r'^(?P<user_id>[0-9]+)/(?P<tile_id>[0-9]+)/solved$', views.tileSolved,name='solved'),
				url(r'^ajaxtest$', views.ajaxTest,name='ajaxtest'),
				url(r'^test$', views.test,name='test')]