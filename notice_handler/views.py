from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
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

@login_required
def contract_manage_search(request):
    if request.method == 'GET':
        hc_res = request.GET.get('host_company_search')
        bc_res = request.GET.get('buyer_company_search')
        sl_res = request.GET.get('store_loc_code_search')
        fn_res = request.GET.get('floor_num_search')
        try:
            if hc_res is None and bc_res is None and sl_res is None and fn_res is None:
                return render(request,'search_contracts.html',{})
            contract = Contract.objects.all()
            if hc_res is not None:
                contract = contract.filter(Q(host_company__company_name__icontains=hc_res))
            if bc_res is not None:
                contract = contract.filter(Q(buyer_company__company_name__icontains=bc_res) )
            if sl_res is not None:
                contract = contract.filter(Q(store_loc_code__icontains=sl_res))
            if fn_res is not None:
                contract = contract.filter(Q(floor_num__icontains=fn_res))
            context = {"contracts":contract}
            return render(request,'search_contracts.html',context)
        except:
            return render(request,'search_contracts.html',{})
    return render(request,'search_contracts.html',{})

@login_required
def contract_manage_check(request, contract_id):
    contract = Contract.objects.filter(id=contract_id)
    first_pn = First_Payment_Notice.objects.filter(contract__id=contract_id)
    periodical_pns = Periodical_Payment_Notice.objects.filter(contract__id=contract_id)
    context = {'contracts' : contract, 'first_payment_notices' : first_pn, 'periodical_payment_notices':periodical_pns}
    return render(request, 'contract_manage_check.html', context)
