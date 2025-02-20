from django import forms

from members.models import Member


class MemForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        # fields = ['name', 'group', 'total_points']

