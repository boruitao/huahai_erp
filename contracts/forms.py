from django import forms
from .models import Contract, Company

class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ('start_date','end_date',)

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('owner_name','owner_address',
        'owner_id','company_name','core_business',)
       
