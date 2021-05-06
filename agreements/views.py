from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.db.models import Q
from contracts.models import Contract, Company, Host, Contract_Status
from notice.models import First_Notice, Periodical_Notice, Notice_Status
from payments.models import Payment, Payment_Status
from datetime import date
from .forms import PerNoticeForm, AgreementForm
from agreements.helper import do_create_agreement_per
from .models import Per_Notice_Pair, First_Notice_Pair, Agreement, Agreement_Status
# Create your views here.
@login_required
def agreement_search_contract(request):
    if request.method == 'GET':
        hc_res = request.GET.get('host_company_search')
        bc_res = request.GET.get('buyer_company_search')
        sl_res = request.GET.get('store_loc_code_search')
        fn_res = request.GET.get('floor_num_search')
        try:
            if hc_res is None and bc_res is None and sl_res is None and fn_res is None:
                return render(request,'agreement/agreement_search_contract.html',{})
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
            return render(request,'agreement/agreement_search_contract.html',context)
        except:
            return render(request,'agreement/agreement_search_contract.html',{})
    return render(request,'agreement/agreement_search_contract.html',{})

@login_required
def create_agreement(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    first_pn = First_Notice.objects.filter(contract__id=contract_id).order_by("notice_id")
    periodical_pns = Periodical_Notice.objects.filter(contract__id=contract_id).order_by("notice_id")
    if request.method != 'POST':
        form = AgreementForm()
    else:
        form = AgreementForm(request.POST)
        if form.is_valid():
            agreement = form.save(commit=False)
            agreement.old_contract = contract
            agreement.cname = contract.buyer_company.company_name
            agreement.created_by = request.user
            agreement.save()
            new_per = Periodical_Notice.objects.filter(Q(contract__id=contract_id) & Q(status=Notice_Status.TMP))
            do_create_agreement_per(new_per, agreement)
            return HttpResponseRedirect(reverse('agreements:all_agreements'))
    context = {'contract' : contract, 'first_notices' : first_pn, 'periodical_notices':periodical_pns, 'form':form}
    return render(request, 'agreement/create_agreement.html', context)

@login_required
def all_agreements(request):
    agreements = Agreement.objects.all().order_by("-date_added")
    context = {"agreements" : agreements}
    return render(request, 'agreement/all_agreements.html', context)

@login_required
def created_agreements(request):
    agreements = Agreement.objects.filter(status=Agreement_Status.CREATED).order_by("-date_added")
    context = {"agreements" : agreements}
    return render(request, 'agreement/created_agreements.html', context)

@login_required
def approved_agreements(request):
    agreements = Agreement.objects.filter(status=Agreement_Status.APPROVED).order_by("-date_added")
    context = {"agreements" : agreements}
    return render(request, 'agreement/approved_agreements.html', context)

@login_required
def unapproved_agreements(request):
    agreements = Agreement.objects.filter(status=Agreement_Status.UNAPPROVED).order_by("-date_added")
    context = {"agreements" : agreements}
    return render(request, 'agreement/unapproved_agreements.html', context)

@login_required
def check_agreement(request, agreement_id):
    agreement = Agreement.objects.get(id=agreement_id)
    per_pairs = Per_Notice_Pair.objects.filter(agreement__id=agreement_id)
    context = {"agreement" : agreement, "per_pairs" : per_pairs}
    return render(request, 'agreement/check_agreement.html', context)

@login_required
def create_agreement_confirm(request, contract_id):
    contract = Contract.objects.get(id=contract_id)
    first_pn = First_Notice.objects.filter(contract__id=contract_id).order_by("notice_id")
    periodical_pns = Periodical_Notice.objects.filter(contract__id=contract_id).order_by("notice_id")
    context = {'contract' : contract, 'first_notices' : first_pn, 'periodical_notices':periodical_pns}
    return render(request, 'agreement/create_agreement.html', context)

@login_required
def create_new_per_notice(request, contract_id, notice_id):
    contract = Contract.objects.get(id=contract_id)
    per_pn = Periodical_Notice.objects.get(id=notice_id)
    old_id = per_pn.id
    old_notice_payed = per_pn.total_amount - per_pn.to_be_payed
    if request.method != 'POST':
        form = PerNoticeForm(instance=per_pn)
    else:
        form = PerNoticeForm(request.POST, instance=per_pn)
        if form.is_valid():
            per_pn.id = None
            per_pn.save()
            new_per_notice = form.save(commit=False)
            new_per_notice.status = Notice_Status.TMP
            new_per_notice.to_be_payed = new_per_notice.total_amount - old_notice_payed
            new_per_notice.save()
            return HttpResponseRedirect(reverse('agreements:create_per_notice_pair_confirm', 
                                    kwargs={'contract_id': contract_id, 
                                    'old_notice_id' : old_id, 
                                    'new_notice_id' : new_per_notice.id}))
    context = {'notice' : per_pn, 'form': form, 'contract':contract}
    return render(request, 'notice_pair/create_new_per_notice.html', context)

@login_required
def create_per_notice_pair_confirm(request, contract_id, old_notice_id, new_notice_id):
    contract = Contract.objects.get(id=contract_id)
    old_pn = Periodical_Notice.objects.get(id=old_notice_id)
    new_pn = Periodical_Notice.objects.get(id=new_notice_id)
    context = {'old_pn' : old_pn, 'new_pn': new_pn, 'contract':contract}
    return render(request, 'notice_pair/create_per_notice_pair_confirm.html', context)

@login_required
def create_per_notice_pair(request, contract_id, old_notice_id, new_notice_id):
    contract = Contract.objects.get(id=contract_id)
    old_per_pn = Periodical_Notice.objects.get(id=old_notice_id)
    new_per_pn = Periodical_Notice.objects.get(id=new_notice_id)
    pair = Per_Notice_Pair.create_pair(old_per_pn, new_per_pn)
    pair.save()
    return HttpResponseRedirect(reverse('agreements:create_agreement', kwargs={'contract_id': contract_id}))

@login_required
def delete_per_pair(request, contract_id, new_notice_id):
    Per_Notice_Pair.objects.filter(new_notice__id=new_notice_id).delete()
    Periodical_Notice.objects.get(id=new_notice_id).delete()
    return HttpResponseRedirect(reverse('agreements:create_agreement', kwargs={'contract_id': contract_id})) 

@login_required
def verify_agreements(request):
    agreements = Agreement.objects.filter(status=Agreement_Status.CREATED)
    context = {"agreements" : agreements}
    return render(request, 'verify_agreements.html', context)
