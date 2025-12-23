from django import forms
from .models import Advertisement

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'content', 'media', 'expiration_date', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'media': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
        }