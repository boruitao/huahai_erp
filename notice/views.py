from .models import First_Notice, Periodical_Notice, PN_Status
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from .forms import FirstNoticeForm
import xlwt
from datetime import date
from django.http import HttpResponse
from notice.excel_helper import create_first_notice, create_periodical_notice

# Create your views here.
@login_required
def active_first_notices(request):
    active_notices = First_Notice.objects.filter(status=PN_Status.ACTIVE)
    inactive_notices = First_Notice.objects.filter(status=PN_Status.PAYED)
    context = {'notices': {'active' : active_notices, 'inactive' : inactive_notices}}
    return render(request, 'first_notices/active_first_notices.html', context)

@login_required
def check_first_notice(request, notice_id):
    notice = First_Notice.objects.get(id=notice_id)
    context = {'notice': notice}
    return render(request, 'first_notices/check_first_notice.html', context)

@login_required
def edit_first_notice(request, notice_id):
    notice = First_Notice.objects.get(id=notice_id)
    contract_id = notice.contract.id
    if request.method != 'POST':
        form = FirstNoticeForm(instance=notice)
    else:
        form = FirstNoticeForm(request.POST, instance=notice)
        if form.is_valid():
            new_notice = form.save(commit=False)
            new_notice.total_amount = new_notice.total_rent + new_notice.promotion_fee
            new_notice.save()  # Save the changes to the database.
            return HttpResponseRedirect(reverse('notice_handler:manage_check_contract', kwargs={'contract_id': contract_id}))
    context = {'notice' : notice, 'form': form}
    return render(request, 'first_notices/edit_first_notice.html', context)

@login_required
def print_first_notice(request, notice_id):
    xlsx_data, nid = create_first_notice(notice_id)
    filename = "first_notice_%s.xls" % nid
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response.write(xlsx_data)
   # return HttpResponseRedirect(reverse('payment:active_notices'))
    return response

@login_required
def approve_first_notice(request, notice_id):
    #TODO: logic behind this
    notice = First_Notice.objects.get(id=notice_id)
    notice.status = PN_Status.PAYED
    notice.date_payed = date.today()
    notice.save()
    return HttpResponseRedirect(reverse('payment:active_first_notices'))

# @login_required
# def all_first_notices(request):
#     notices = Periodical_Notice.objects.all()
#     context = {'notices': notices}
#     return render(request, 'notices/all_periodical_notices.html', context)

@login_required
def all_periodical_notices(request):
    notices = Periodical_Notice.objects.all()
    context = {'notices': notices}
    return render(request, 'periodical_notices/all_periodical_notices.html', context)

@login_required
def check_periodical_notice(request, notice_id):
    notice = Periodical_Notice.objects.get(id=notice_id)
    context = {'notice': notice}
    return render(request, 'periodical_notices/check_periodical_notice.html', context)


# @login_required
# def edit_periodical_notice(request, notice_id):
    

@login_required
def print_periodical_notice(request, notice_id):
    xlsx_data, nid, pnum = create_periodical_notice(notice_id)
    filename = "periodical_notice_%s_%d.xls" % (nid, pnum)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response.write(xlsx_data)
   # return HttpResponseRedirect(reverse('payment:active_notices'))
    return response