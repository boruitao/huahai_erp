from .models import Payment_Notice
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404

# Create your views here.
@login_required
def active_payment_notices(request):
    notices = Payment_Notice.objects.filter(is_active=True)
    context = {'payment_notices': notices}
    return render(request, 'payment_notices/active_payment_notices.html', context)

@login_required
def check_payment_notice(request, payment_notice_id):
    notice = Payment_Notice.objects.get(id=payment_notice_id)
    context = {'payment_notice': notice}
    return render(request, 'payment_notices/check_payment_notice.html', context)