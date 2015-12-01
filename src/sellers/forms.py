from django import forms


class NewSellerForm(forms.Form):
	agree = forms.BooleanField(label='Agree to Terms', widget=forms.CheckboxInput)