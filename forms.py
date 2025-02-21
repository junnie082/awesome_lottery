from django import forms

from dashboard.models import Dashboard
from members.models import Member


class MemForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = '__all__'



