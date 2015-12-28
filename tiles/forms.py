from django import forms

from .models import Tile

class TileForm(forms.ModelForm):
	
	class Meta:

		model = Tile
		fields = ('content',)