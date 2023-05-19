from django import forms

from .models import ecommerce


class movieform (forms.ModelForm):
    class Meta:
        model=ecommerce
        fields=["name","price","brand","size","details","image"]
