from django import forms
from .models import Contract, Company, Host
#from bootstrap_datepicker_plus import DatePickerInput

class ContractForm(forms.ModelForm):
    host_company = forms.ModelChoiceField(queryset=Host.objects.all(), to_field_name='company_name')
    class Meta:
        model = Contract
        fields = ('start_date','end_date','sign_date','floor_num','store_loc_code','region',
        'unit_price','area','monthly_price','yearly_price','total_price','payment_cycle','num_cycle','business','category',
        'promotion_price','deposit','perf_bond','water_bill','elect_bill','host_company')
        # widgets = {
        #     'start_date': DatePickerInput(), # default date-format %m/%d/%Y will be used
        #     'end_date': DatePickerInput(), # specify date-frmat
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['sign_date'].widget.attrs.update({'class': 'form-control'})
        self.fields['floor_num'].widget.attrs.update({'class': 'form-control'})
        self.fields['store_loc_code'].widget.attrs.update({'class': 'form-control'})
        self.fields['region'].widget.attrs.update({'class': 'form-control'})
        self.fields['unit_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['area'].widget.attrs.update({'class': 'form-control'})
        self.fields['monthly_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['yearly_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['total_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['payment_cycle'].widget.attrs.update({'class': 'form-control'})
        self.fields['num_cycle'].widget.attrs.update({'class': 'form-control'})
        self.fields['business'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['promotion_price'].widget.attrs.update({'class': 'form-control'})
        self.fields['deposit'].widget.attrs.update({'class': 'form-control'})
        self.fields['perf_bond'].widget.attrs.update({'class': 'form-control'})
        self.fields['water_bill'].widget.attrs.update({'class': 'form-control'})
        self.fields['elect_bill'].widget.attrs.update({'class': 'form-control'})
        self.fields['host_company'].widget.attrs.update({'class': 'form-select'})

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('owner_name','owner_address',
        'owner_id','company_name','core_business',)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['owner_address'].widget.attrs.update({'class': 'form-control'})
        self.fields['owner_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['company_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['core_business'].widget.attrs.update({'class': 'form-control'})
        
class HostForm(forms.ModelForm):
    class Meta:
        model = Host
        fields = ('owner_name','address','city','company_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['owner_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['city'].widget.attrs.update({'class': 'form-control'})
        self.fields['company_name'].widget.attrs.update({'class': 'form-control'})

       
