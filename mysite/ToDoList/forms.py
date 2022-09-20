from .models import List
from django import forms

class index_form (forms.ModelForm):
	class Meta:
		model =  List
		fields = ["task"]
