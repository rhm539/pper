from django import forms

from setup.models import buyer


##
class BuyerForm(forms.ModelForm):
    class Meta:
        model = buyer
        labels = {
            'name': 'Buyer Name',
            'shortcut': 'Nick Name',
            'address': 'Address',
        }
        fields = [
            'name',
            'shortcut',
            'address',
        ]
