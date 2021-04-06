from django import forms
from .models import Payment
#from bootstrap_datepicker_plus import DatePickerInput

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('pay_method','amount','reason', 'payment_id', 'date_received')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pay_method'].widget.attrs.update({'class': 'form-control'})
        self.fields['amount'].widget.attrs.update({'class': 'form-control'})
        self.fields['reason'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_received'].widget.attrs.update({'class': 'form-control'})