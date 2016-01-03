from django import forms
from django.contrib.auth.models import User


from .models import Tile

class TileForm(forms.ModelForm):
	
	class Meta:

		model = Tile
		fields = ('content',)

class RegForm(forms.ModelForm):
	
	class Meta:

		model = User
		fields = ('username','password')

