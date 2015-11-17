from django import forms


class ProductAddForm(forms.Form):
	title = forms.CharField()
	description = forms.CharField() #this might be a problem
	price  = forms.DecimalField()


