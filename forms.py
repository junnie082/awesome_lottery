from django import forms

from lottery.models import Member


class MemForm(forms.ModelForm):
    class Meta:
        model = Member
        # fields = '__all__'
        fields = ['name', 'points', 'group']

