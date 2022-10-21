from django import forms
from plan.models import plan
from production.models import production
from setup.models import *
##


class PlanForm(forms.ModelForm):
    buyer = forms.ModelChoiceField(queryset=buyer.objects.order_by('name'))
    style = forms.ModelChoiceField(queryset=style.objects.order_by('name'))

    class Meta:
        model = plan
        fields = ['buyer', 'style', 'deleveryDate', 'inputDate',
                  'sewingEndDate', 'orderQty', 'planQtyExtra']
        widgets = {
            'deleveryDate': forms.DateInput({'type': 'date'}),
            'inputDate': forms.DateInput({'type': 'date'}),
            'sewingEndDate': forms.DateInput({'type': 'date'}),
        }
        labels = {
            'deleveryDate': 'Delevery Date',
            'inputDate': 'Input Date',
            'sewingEndDate': 'Sewing End Date',
            'orderQty': 'Order Qty.',
            'planQtyExtra': 'Plan Qty. Extra',
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['style'].queryset = style.objects.none()

            if 'buyer' in self.data:
                try:
                    buyer = int(self.data.get('buyer'))
                    self.fields['style'].queryset = style.objects.filter(
                        buyer=buyer).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty City queryset
            elif self.instance.pk:
                self.fields['style'].queryset = self.instance.buyer.style_set.order_by(
                    'name')


class planAddForms(forms.ModelForm):
    line = forms.ModelChoiceField(queryset=line.objects.order_by('name'))

    class Meta:
        model = production
        fields = ['line', 'style', 'operator', 'helper',
                  'runDay', 'workHour', 'dayTarget']
        widgets = {
            'line': forms.TextInput(attrs={'readonly': 'readonly'})
        }
