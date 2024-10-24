from django import forms
from .models import Property


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        widgets = {
            'date_published': forms.DateInput(attrs={'type': 'date'}),
            'amenities': forms.Textarea(attrs={'rows': 3}),
            'requirements': forms.Textarea(attrs={'rows': 3}),
            'comments': forms.Textarea(attrs={'rows': 3}),
            'property_description': forms.Textarea(attrs={'rows': 5}),
        }