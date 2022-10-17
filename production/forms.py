from django import forms

from production.models import *


##
class productionHourForm(forms.ModelForm):
    class Meta:
        model = production
        fields = [
            'H_8_9',
            'H_9_10',
            'H_10_11',
            'H_11_12',
            'H_12_13',
            'H_14_15',
            'H_15_16',
            'H_16_17',
            'H_17_18',
            'H_18_19',
            'H_19_20',
            'H_20_21',
            'H_21_22',
            'LineWIP',
            'dataLock',
        ]
        labels = {
            'H_8_9': '8AM to 9AM',
            'H_9_10':  '9AM to 10AM',
            'H_10_11': '10AM to 11AM',
            'H_11_12': '11AM to 12PM',
            'H_12_13': '12PM to 1PM',
            'H_14_15': '2PM to 3PM',
            'H_15_16': '3PM to 4PM',
            'H_16_17': '4PM to 5PM',
            'H_17_18': '5PM to 6PM',
            'H_18_19': '6PM to 7PM',
            'H_19_20': '7PM to 8PM',
            'H_20_21': '8PM to 9PM',
            'H_21_22': '9PM to 10PM',
            'LineWIP': 'Line WIP',
            'dataLock': 'Data Lock',
        }
