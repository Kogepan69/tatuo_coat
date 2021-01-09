from django import forms


class CarForm(forms.Form):
    name = forms.CharField(max_length=100, label='車種')