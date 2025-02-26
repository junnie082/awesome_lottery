from django import forms

from dashboard.models import Dashboard
from members.models import Member


class MemForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        # Ensure mem_time and mem_level are valid strings
        mem_time = cleaned_data.get('mem_time')
        mem_level = cleaned_data.get('mem_level')

        if mem_time:
            cleaned_data['mem_time'] = str(mem_time)
        if mem_level:
            cleaned_data['mem_level'] = str(mem_level)

        return cleaned_data  # Return modified data

class DashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = '__all__'



