from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.http import Http404
from contracts.models import Contract, Company, Host, Contract_Status
from notice.models import First_Notice, Periodical_Notice, Notice_Status
from payments.models import Payment, Payment_Status
from agreements.models import Agreement, Agreement_Status, Per_Notice_Pair
from datetime import date
from notice_handler.notice_creator import generate_first_notice, generate_periodical_notices
from background_task import background

#后台更新超期款
@background(schedule=60)
def update_notice_status():
    # lookup user by id and send them a message
    today = date.today()
    all_active_notice = Periodical_Notice.objects.filter(status=Notice_Status.ACTIVE)
    print("------- 检查是否有超期款 --------")
    for notice in all_active_notice:
        if notice.deadline <= today:
            notice.status = Notice_Status.OVERDUE
            print("------- %s 为超期款 --------" % notice.notice_id)
    print("------- 检查完毕 --------")


# Create your views here.
@login_required
def approve_contract(request, contract_id):
    today = date.today()
    contract = Contract.objects.get(id=contract_id)
    # change contract status
    contract.status = Contract_Status.APPROVED
    contract.approved_by = request.user
    contract.date_approved = today

    # assign contract id
    date_str = (contract.sign_date.year - 2000) * 10000 + contract.sign_date.month * 100 + contract.sign_date.day
    date_str = date_str * 1000 + Contract.objects.filter(status=Contract_Status.APPROVED, host_company__id=contract.host_company.id, sign_date=contract.sign_date).count()+1
    contract.contract_id = "{:02d}".format(contract.host_company.id) + str(date_str) 
    contract.save()
    
    # generate corresponding notices
    count_notice = First_Notice.objects.filter(date_released__year=today.year, date_released__month=today.month, date_released__day=today.day).count()+1
    generate_first_notice(contract, count_notice)
    generate_periodical_notices(contract)

    return HttpResponseRedirect(reverse('contracts:verify_contracts'))

@login_required
def approve_payment(request, payment_id):
    today = date.today()
    payment = Payment.objects.get(id=payment_id)
    payment.status = Payment_Status.APPROVED
    payment.approved_by = request.user
    payment.date_approved = today
    payment.save()

    pn = First_Notice.objects.get(id=payment.first_notice.id) if payment.is_first else Periodical_Notice.objects.get(id=payment.per_notice.id)
    #     return HttpResponseRedirect(reverse('payments:verify_single_payment',kwargs={'payment_id': payment_id}))
    pn.to_be_payed = pn.to_be_payed - payment.amount

    if pn.to_be_payed <= 0:
        if payment.is_first:
            Payment.objects.filter(first_notice__id=pn.id).exclude(id=payment_id).update(status=Payment_Status.ANNULLED)
        elif payment.is_per:
            Payment.objects.filter(per_notice__id=pn.id).exclude(id=payment_id).update(status=Payment_Status.ANNULLED)
        pn.status = Notice_Status.PAYED
        pn.date_payed = date.today()
    pn.save()

     # change contract to_be_payed
    contract = Contract.objects.get(id=pn.contract.id)
    contract.to_be_payed = contract.to_be_payed - payment.amount
    
    if contract.to_be_payed <= 0:
        contract.status = Contract_Status.COMPLETED
        contract.date_completed = date.today()
    contract.save()
        
    return HttpResponseRedirect(reverse('payments:verify_payments'))

@login_required
def approve_agreement(request, agreement_id):
    agreement = Agreement.objects().get(id=agreement_id)
    

@login_required
def unapprove_contract(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    contract.status = Contract_Status.UNAPPROVED
    contract.save()
    return HttpResponseRedirect(reverse('contracts:all_contracts'))

@login_required
def unapprove_payment(request, payment_id):
    payment = Payment.objects.get(id=payment_id)
    payment.status = Payment_Status.UNAPPROVED
    payment.save()
    return HttpResponseRedirect(reverse('payments:all_payments'))

# @login_required
# def manage_search_contract(request):
#     if request.method == 'GET':
#         hc_res = request.GET.get('host_company_search')
#         bc_res = request.GET.get('buyer_company_search')
#         sl_res = request.GET.get('store_loc_code_search')
#         fn_res = request.GET.get('floor_num_search')
#         try:
#             if hc_res is None and bc_res is None and sl_res is None and fn_res is None:
#                 return render(request,'manage_search_contracts.html',{})
#             contract = Contract.objects.filter(status=Contract_Status.APPROVED)
#             if hc_res is not None:
#                 contract = contract.filter(Q(host_company__company_name__icontains=hc_res))
#             if bc_res is not None:
#                 contract = contract.filter(Q(buyer_company__company_name__icontains=bc_res) )
#             if sl_res is not None:
#                 contract = contract.filter(Q(store_loc_code__icontains=sl_res))
#             if fn_res is not None:
#                 contract = contract.filter(Q(floor_num__icontains=fn_res))
#             context = {"contracts":contract}
#             return render(request,'manage_search_contracts.html',context)
#         except:
#             return render(request,'manage_search_contracts.html',{})
#     return render(request,'manage_search_contracts.html',{})

# @login_required
# def manage_check_notices(request, contract_id):
#     contract = Contract.objects.filter(id=contract_id)
#     first_pn = First_Notice.objects.filter(contract__id=contract_id)
#     periodical_pns = Periodical_Notice.objects.filter(contract__id=contract_id)
#     context = {'contracts' : contract, 'first_notices' : first_pn, 'periodical_notices':periodical_pns}
#     return render(request, 'manage_check_notices.html', context)
