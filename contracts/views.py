from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from .models import Contract, Company
from .forms import ContractForm, CompanyForm
# Create your views here.
def home(request):
    return render(request, 'base.html')

# @login_required
# def contracts(request):
#     contracts = Contract.objects.filter(owner=request.user).order_by('-sign_date')
#     context = {'contracts': contracts}
#     return render(request, 'contracts/all_contracts.html', context)

# @login_required
# def contract(request, contract_id):
#     contract = Contract.objects.get(id=contract_id)
#     if contract.owner != request.user:
#         raise Http404
#     context = {'contract': contract}
#     return render(request, 'contracts/contract.html', context)

# @login_required
# def new_contract(request, company_id):
#     company = Company.objects.get(id=company_id)
#     if request.method != 'POST':
#         form = ContractForm()
#     else:
#         form = ContractForm(request.POST)
#         if form.is_valid():
#             new_contract = form.save(commit=False)
#             new_contract.owner = request.user  # Set contracts owner attribute to current user.
#             new_contract.company = company
#             new_contract.save()  # Save the changes to the database.
#             return HttpResponseRedirect(reverse('contracts:contracts', args=[company_id]))
#     context = {'company' : company, 'form': form}
#     return render(request, 'contracts/add_new_contract.html', context)

# @login_required
# def companies(request):
#     companies = Company.objects.order_by('date_added')
#     context = {'companies': companies}
#     return render(request, 'companies/all_companies.html', context)

# @login_required
# def company(request, company_id):
#     company = Company.objects.get(id=company_id)
#     contracts = company.contract_set.order_by('-date_added')
#     context = {'company': company, 'contracts': contracts}
#     return render(request, 'companies/company.html', context)

# @login_required
# def new_company(request):
#     if request.method != 'POST':
#         form = CompanyForm()
#     else:
#         form = CompanyForm(request.POST)
#         if form.is_valid():
#             new_company = form.save(commit=False)  # Save contract in a variable.
#             new_company.save()  # Save the changes to the database.
#             return HttpResponseRedirect(reverse('contracts:companies'))

#     context = {'form': form}
#     return render(request, 'contracts/add_new_company.html', context)
    