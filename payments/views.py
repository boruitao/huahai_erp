from django.shortcuts import render
from notice.models import First_Notice, Periodical_Notice
from contracts.models import Contract, Contract_Status
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse
from django.http import Http404
from .forms import PaymentForm
from .models import Payment
from datetime import date
# Create your views here.
@login_required
def create_payment(request, notice_id, is_first):
    notice = First_Notice.objects.get(id=notice_id)
    # if is_first == 0:
    #     notice = First_Notice.objects.get(id=notice_id)
    if is_first == 1:
        notice = Periodical_Notice.objects.get(id=notice_id)
    if request.method != 'POST':
        form = PaymentForm()
    else:
        form = PaymentForm(request.POST)
        if form.is_valid():
            new_payment = form.save(commit=False)
            if is_first == 0:
                new_payment.first_notice = notice
                new_payment.is_first = True
            elif is_first == 1:
                new_payment.per_notice = notice
                new_payment.is_per = True
            new_payment.created_by = request.user
            new_payment.cname = notice.cname
            new_payment.save()
            return HttpResponseRedirect(reverse('payments:all_payments'))
    context = {'notice' : notice, 'form': form, 'is_first' : is_first}
    return render(request, 'create_payment.html', context)

@login_required
def create_periodical_payment(request, notice_id):
    notice = Periodical_Notice.objects.get(id=notice_id)
    if request.method != 'POST':
        form = PaymentForm()
    else:
        form = PaymentForm(request.POST)
        if form.is_valid():
            new_payment = form.save(commit=False)
            new_payment.first_notice = notice
            new_payment.created_by = request.user  # Set contracts owner attribute to current user.
            new_payment.cname = notice.cname
            new_payment.is_per = True
            new_payment.save()  # Save the changes to the database.
            return HttpResponseRedirect(reverse('payments:create_periodical_payment'))
    context = {'notice' : notice, 'form': form}
    return render(request, 'payment/create_payment.html', context)

@login_required
def payment_search_contract(request):
    if request.method == 'GET':
        hc_res = request.GET.get('host_company_search')
        bc_res = request.GET.get('buyer_company_search')
        sl_res = request.GET.get('store_loc_code_search')
        fn_res = request.GET.get('floor_num_search')
        try:
            if hc_res is None and bc_res is None and sl_res is None and fn_res is None:
                return render(request,'payment_search_contract.html',{})
            contract = Contract.objects.filter(status=Contract_Status.APPROVED)
            if hc_res is not None:
                contract = contract.filter(Q(host_company__company_name__icontains=hc_res))
            if bc_res is not None:
                contract = contract.filter(Q(buyer_company__company_name__icontains=bc_res) )
            if sl_res is not None:
                contract = contract.filter(Q(store_loc_code__icontains=sl_res))
            if fn_res is not None:
                contract = contract.filter(Q(floor_num__icontains=fn_res))
            context = {"contracts":contract}
            return render(request,'payment_search_contract.html',context)
        except:
            return render(request,'payment_search_contract.html',{})
    return render(request,'payment_search_contract.html',{})

@login_required
def payment_check_notices(request, contract_id):
    contract = Contract.objects.filter(id=contract_id)
    first_pn = First_Notice.objects.filter(contract__id=contract_id)
    periodical_pns = Periodical_Notice.objects.filter(contract__id=contract_id)
    context = {'contracts' : contract, 'first_notices' : first_pn, 'periodical_notices':periodical_pns}
    return render(request, 'payment_check_notices.html', context)

@login_required
def all_payments(request):
    payments = Payment.objects.all().order_by('-date_added')
    context = {'payments' : payments}
    return render(request, 'all_payments.html', context)

# @login_required
# def all_created_contracts(request):
#     contracts = Contract.objects.filter(status=Contract_Status.CREATED).order_by('-sign_date')
#     context = {'contracts': contracts}
#     return render(request, 'contracts/all_created_contracts.html', context)

# @login_required
# def all_approved_contracts(request):
#     contracts = Contract.objects.filter(status=Contract_Status.APPROVED).order_by('-sign_date')
#     context = {'contracts': contracts}
#     return render(request, 'contracts/all_approved_contracts.html', context)

# @login_required
# def all_unapproved_contracts(request):
#     contracts = Contract.objects.filter(status=Contract_Status.UNAPPROVED).order_by('-sign_date')
#     context = {'contracts': contracts}
#     return render(request, 'contracts/all_unapproved_contracts.html', context)
