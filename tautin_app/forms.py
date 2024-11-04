from tautin_app.models import Link
from django import forms
from django.core.exceptions import ValidationError
class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('long_link', 'short_url_link_address')
        
        widgets = {
            'long_link' : forms.TextInput(attrs={'type' : 'text'}),
            'short_url_link_address' : forms.TextInput(attrs={'type' : 'text'}),
        }
        
    def clean_short_url_link_address(self):
        short_url_link_address = self.cleaned_data.get('short_url_link_address')
        
        # Memeriksa apakah short_url_link_address sudah ada
        if Link.objects.filter(short_url_link_address=short_url_link_address).exists():
            # print('error')
            raise ValidationError("Short URL Link Address already used. Please use another URL!")
        
        return short_url_link_address