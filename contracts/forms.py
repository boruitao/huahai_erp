from django import forms
from .models import Contract, Company

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['text']
        labels = {'text': ''}


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

