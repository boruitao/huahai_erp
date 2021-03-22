from django import forms
from .models import First_Payment_Notice
#from bootstrap_datepicker_plus import DatePickerInput

class FirstPaymentNoticeForm(forms.ModelForm):
    class Meta:
        model = First_Payment_Notice
        fields = ('deadline','promotion_fee','total_rent')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs.update({'class': 'form-control'})
        self.fields['promotion_fee'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_rent'].widget.attrs.update({'class': 'form-control'})