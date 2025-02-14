from django import forms

class NameForm(forms.Form):
    mem_name = forms.CharField(label="Your name", max_length=100)