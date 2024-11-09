from tautin_app.models import Link
from django import forms
from django.core.exceptions import ValidationError

from tautin_app import urls as tautin_app_url
from tautin import urls as tautin_url
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
        
        if self.instance.pk:
            if Link.objects.filter(short_url_link_address=short_url_link_address).exclude(pk=self.instance.pk).exists():
                raise ValidationError("Short URL Link Address already used. Please use another URL!")
        else:
            if Link.objects.filter(short_url_link_address=short_url_link_address).exists():
                raise ValidationError("Short URL Link Address already used. Please use another URL!")
            
        if short_url_link_address in tautin_app_url.url_list.keys() or short_url_link_address in tautin_app_url.url_list.values() or short_url_link_address in tautin_url.url_list.keys() or short_url_link_address in tautin_url.url_list.values():
            raise ValidationError("Short URL Link Address already used. Please use another URL!")
        return short_url_link_address