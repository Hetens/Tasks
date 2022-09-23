from django import forms

class Queryform(forms.Form):
    yourquery = forms.CharField(label='Your query', max_length=100)