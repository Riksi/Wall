from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.welcome,name='welcome'),url(r'^(?P<user_id>[0-9]+)/tiles$', views.myTiles,name='myTiles'), url(r'^(?P<user_id>[0-9]+)/settings$', views.settings,name='settings')]