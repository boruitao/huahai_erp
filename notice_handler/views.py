from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from contracts.models import Contract, Company, Host
from payment.models import First_Payment_Notice, Periodical_Payment_Notice
from datetime import date
from notice_handler.notice_creator import generate_first_payment_notice, generate_periodical_payment_notices

# Create your views here.
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