from django import forms

class InputForm(forms.Form):
    word = forms.CharField(max_length = 200)