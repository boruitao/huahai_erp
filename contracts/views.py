from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from .models import Contract, Company
from payment.models import Payment_Notice
from .forms import ContractForm, CompanyForm
from datetime import date
from contracts.form_generator import generate_first_payment_notice

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
    contract.save()
    
    #now = datetime.datetime.now()
    #count = Payment_Notice.objects.filter(date_released.date=now.date).filter(date_released.month=now.month).filter(date_released.year=now.year)+1
    today = date.today()
    count = Payment_Notice.objects.filter(date_released__year=today.year).count()+1
    pn = generate_first_payment_notice(contract, count)
    pn.save()
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
            new_contract.company = company
            new_contract.save()  # Save the changes to the database.
            return HttpResponseRedirect(reverse('contracts:all_contracts'))
    context = {'company' : company, 'form': form}
    return render(request, 'contracts/add_new_contract.html', context)

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
    