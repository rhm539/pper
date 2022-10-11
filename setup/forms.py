from django import forms

from setup.models import *


##
class BuyerForm(forms.ModelForm):
    class Meta:
        model = buyer
        labels = {
            'name': '',
            'shortcut': '',
            'address': '',
        }
        fields = [
            'name',
            'shortcut',
            'address',
        ]


class StyleForm(forms.ModelForm):
    class Meta:
        model = style
        labels = {
            'name': '',
            'buyer': '',
            'smv': '',
        }
        fields = [
            'name',
            'buyer',
            'smv',
        ]
