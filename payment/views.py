from .models import First_Payment_Notice, Periodical_Payment_Notice
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from .forms import FirstPaymentNoticeForm
import xlwt
from django.http import HttpResponse
from payment.excel_helper import create_first_payment_notice

# Create your views here.
@login_required
def active_first_payment_notices(request):
    notices = First_Payment_Notice.objects.filter(is_active=True)
    context = {'payment_notices': notices}
    return render(request, 'first_payment_notices/active_first_payment_notices.html', context)

@login_required
def check_first_payment_notice(request, payment_notice_id):
    notice = First_Payment_Notice.objects.get(id=payment_notice_id)
    context = {'payment_notice': notice}
    return render(request, 'first_payment_notices/check_first_payment_notice.html', context)

@login_required
def edit_first_payment_notice(request, payment_notice_id):
    notice = First_Payment_Notice.objects.get(id=payment_notice_id)
    if request.method != 'POST':
        form = FirstPaymentNoticeForm(instance=notice)
    else:
        form = FirstPaymentNoticeForm(request.POST, instance=notice)
        if form.is_valid():
            new_notice = form.save(commit=False)
            new_notice.total_amount = new_notice.total_rent + new_notice.promotion_fee
            new_notice.save()  # Save the changes to the database.
            return HttpResponseRedirect(reverse('payment:active_first_payment_notices'))
    context = {'payment_notice' : notice, 'form': form}
    return render(request, 'first_payment_notices/edit_first_payment_notice.html', context)

@login_required
def print_first_payment_notice(request, payment_notice_id):
    xlsx_data, nid = create_first_payment_notice(payment_notice_id)
    filename = "first_notice_%s.xls" % nid
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    response.write(xlsx_data)
   # return HttpResponseRedirect(reverse('payment:active_payment_notices'))
    return response

@login_required
def all_periodical_payment_notices(request):
    notices = Periodical_Payment_Notice.objects.all()
    context = {'payment_notices': notices}
    return render(request, 'payment_notices/all_periodical_payment_notices.html', context)

# @login_required
# def check_periodical_payment_notice(request, payment_notice_id):


# @login_required
# def edit_periodical_payment_notice(request, payment_notice_id):
    

# @login_required
# def print_periodical_payment_notice(request, payment_notice_id):
