from django import forms
from .models import Newappdetails

class Newappform(forms.ModelForm):
	
	class Meta:
		model = Newappdetails
		fields = ('title','content')

