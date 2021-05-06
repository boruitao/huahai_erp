from django import forms
from notice.models import Periodical_Notice
from .models import Per_Notice_Pair, First_Notice_Pair, Agreement
#from bootstrap_datepicker_plus import DatePickerInput

class PerNoticeForm(forms.ModelForm):
    class Meta:
        model = Periodical_Notice
        fields = ('deadline','total_amount','payment_start_date', 'payment_end_date')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deadline'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_end_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_amount'].widget.attrs.update({'class': 'form-control'})

class AgreementForm(forms.ModelForm):
    class Meta:
        model = Agreement
        fields = ('reason',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['reason'].widget.attrs.update({'class': 'form-control'})

# class NoticePairForm(forms.ModelForm):
#     class Meta: 
#         model = Notice_Pair