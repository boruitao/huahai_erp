from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from .models import Contract, Company, Host
from payment.models import First_Payment_Notice, Periodical_Payment_Notice
from .forms import ContractForm, CompanyForm, HostForm
from datetime import date
from contracts.form_generator import generate_first_payment_notice, generate_periodical_payment_notices

# Create your views here.
@login_required(login_url='/users/login/')
def home(request):
    return render(request, 'base.html')

@login_required
def all_contracts(request):
    contracts = Contract.objects.filter(created_by=request.user).order_by('-sign_date')
    context = {'contracts': contracts}
    return render(request, 'contracts/all_contracts.html', context)

@login_required
def unapproved_contracts(request):
    contracts = Contract.objects.filter(approved_by_manager=False).order_by('-sign_date')
    context = {'contracts': contracts}
    return render(request, 'contracts/unapproved_contracts.html', context)

@login_required
def approve_contract(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    contract.approved_by_manager = True
    date_str = (contract.sign_date.year - 2000) * 10000 + contract.sign_date.month * 100 + contract.sign_date.day
    date_str = date_str * 1000 + Contract.objects.filter(approved_by_manager=True, host_company__id=contract.host_company.id, sign_date=contract.sign_date).count()+1
    contract.contract_id = "{:02d}".format(contract.host_company.id) + str(date_str) 
    contract.save()
    
    today = date.today()
    count_notice = First_Payment_Notice.objects.filter(date_released__year=today.year, date_released__month=today.month, date_released__day=today.day).count()+1
    first_pn = generate_first_payment_notice(contract, count_notice)
    first_pn.save()

    generate_periodical_payment_notices(contract)
    return HttpResponseRedirect(reverse('contracts:unapproved_contracts'))

@login_required
def contract(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    context = {'contract': contract}
    return render(request, 'contracts/contract.html', context)

@login_required
def new_contract(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method != 'POST':
        form = ContractForm()
    else:
        form = ContractForm(request.POST)
        if form.is_valid():
            new_contract = form.save(commit=False)
            new_contract.created_by = request.user  # Set contracts owner attribute to current user.
            new_contract.buyer_company = company
            new_contract.save()  # Save the changes to the database.
            return HttpResponseRedirect(reverse('contracts:all_contracts'))
    context = {'company' : company, 'form': form}
    return render(request, 'contracts/add_new_contract.html', context)

@login_required
def new_host(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            new_host = form.save(commit=False)
            new_host.save()  # Save the changes to the database.
            return HttpResponseRedirect(reverse('contracts:new_contract',  kwargs={'company_id': company_id}))
    form = HostForm()
    context = {'company' : company, 'form': form}
    return render(request, 'hosts/add_new_host.html', context)

@login_required
def all_companies(request):
    companies = Company.objects.order_by('date_added')
    context = {'companies': companies}
    return render(request, 'companies/all_companies.html', context)

@login_required
def company(request, company_id):
    company = Company.objects.get(id=company_id)
    context = {'company': company}
    return render(request, 'companies/company.html', context)

@login_required
def new_company(request):
    if request.method != 'POST':
        form = CompanyForm()
    else:
        form = CompanyForm(request.POST)
        if form.is_valid():
            new_company = form.save(commit=False)  # Save contract in a variable.
            new_company.save()  # Save the changes to the database.
            return HttpResponseRedirect(reverse('contracts:all_companies'))

    context = {'form': form}
    return render(request, 'companies/add_new_company.html', context)
    