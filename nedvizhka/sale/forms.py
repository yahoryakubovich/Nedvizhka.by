from django import forms
from .models import *


class FlatForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['description'].widget.attrs.update(size='40')

    class Meta:
        model = Flat
        exclude = ['is_moderated', 'creator']
