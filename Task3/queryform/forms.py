from django import forms

class Queryform(forms.Form):
    query = forms.CharField(label='Your query', max_length=100)