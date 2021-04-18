from django.shortcuts import render
from notice.models import First_Notice, Periodical_Notice, Notice_Status
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
from django.db.models import Q, Sum
import xlwt
import sys
from datetime import date
from django.http import HttpResponse

# Create your views here.
@login_required
def check_receivables(request):
    today = date.today()
    notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.ACTIVE), 
                            Q(deadline__year=today.year) & Q(deadline__month=today.month) |
                            Q(date_released__year=today.year) & Q(date_released__month=today.month)
                            )
    total_amount = notices.aggregate(Sum('total_amount'))
    print(str(total_amount))
    context = {'notices': notices, 'year':today.year, 'month':today.month,'title':'%d年%d月应收款'%(today.year,today.month)}
    return render(request, 'receivables/check_receivables.html', context)

@login_required
def search_receivables_notices(request):
    template_name = 'receivables/check_receivables.html'
    today = date.today()
    title = '本月(%d年%d月)应收款'%(today.year,today.month)
    notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.ACTIVE),
                            Q(deadline__year=today.year) & Q(deadline__month=today.month) |
                            Q(date_released__year=today.year) & Q(date_released__month=today.month)
                            ).order_by('notice_id')
    context = {"notices": notices, 'year':today.year, 'month':today.month, 'title':title}
    if request.method == 'GET':
        year_res = request.GET.get('year_search')
        month_res = request.GET.get('month_search')
        try:
            if not year_res and not month_res:
                return render(request, template_name, context)
            elif not year_res:
                notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.ACTIVE),
                                            Q(deadline__year=today.year) & Q(deadline__month=month_res) |
                                            Q(date_released__year=today.year) & Q(date_released__month=month_res)).order_by('notice_id')
                title ='%s年%s月年应收款'% (today.year, month_res)
                total = notices.aggregate(Sum('total_amount'))
                context = {"notices": notices, 'year':today.year,'month':month_res, 'title':title,'total_amount':total }
            elif not month_res:
                notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.ACTIVE),
                                                        Q(deadline__year=year_res) |
                                                        Q(date_released__year=year_res)).order_by('notice_id')
                total = notices.aggregate(Sum('total_amount'))
                context = {"notices": notices, 'year':year_res, 'title':'%s年应收款'%year_res, 'total_amount':total}
            else: # month_res is not None:
                notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.ACTIVE),
                                            Q(deadline__year=year_res) & Q(deadline__month=month_res) |
                                            Q(date_released__year=year_res) & Q(date_released__month=month_res)).order_by('notice_id')
                title = '%s年%s月年应收款'% (year_res, month_res)
                total = notices.aggregate(Sum('total_amount'))
                context = {"notices": notices, 'year':year_res,'month':month_res, 'title': title, 'total_amount':total }
            return render(request,template_name,context)
        except:
            print("Unexpected error:", sys.exc_info())
            return render(request,template_name,context)
    return render(request,template_name,context)


@login_required
def check_overdue(request):
    notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.OVERDUE))
    total_amount = notices.aggregate(Sum('total_amount'))
    context = {'notices': notices, 'title':'超期款'}
    return render(request, 'overdue/check_overdue.html', context)

@login_required
def search_overdue_notices(request):
    template_name = 'overdue/check_overdue.html'
    today = date.today()
    title = '本月(%d年%d月)超期款'%(today.year,today.month)
    notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.OVERDUE),
                            Q(deadline__year=today.year) & Q(deadline__month=today.month)
                            ).order_by('notice_id')
    context = {"notices": notices, 'year':today.year, 'month':today.month, 'title':title}
    if request.method == 'GET':
        year_res = request.GET.get('year_search')
        month_res = request.GET.get('month_search')
        try:
            if not year_res and not month_res:
                return render(request, template_name, context)
            elif not year_res:
                notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.OVERDUE),
                                            Q(deadline__year=today.year) & Q(deadline__month=month_res)
                                            ).order_by('notice_id')
                title ='%s年%s月年超期款'% (today.year, month_res)
                total = notices.aggregate(Sum('total_amount'))
                context = {"notices": notices, 'year':today.year,'month':month_res, 'title':title,'total_amount':total }
            elif not month_res:
                notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.OVERDUE),
                                                        Q(deadline__year=year_res)
                                                        ).order_by('notice_id')
                total = notices.aggregate(Sum('total_amount'))
                context = {"notices": notices, 'year':year_res, 'title':'%s年超期款'%year_res, 'total_amount':total}
            else:
                notices = Periodical_Notice.objects.filter(Q(status=Notice_Status.OVERDUE),
                                            Q(deadline__year=year_res) & Q(deadline__month=month_res)
                                           ).order_by('notice_id')
                title = '%s年%s月年超期款'% (year_res, month_res)
                total = notices.aggregate(Sum('total_amount'))
                context = {"notices": notices, 'year':year_res,'month':month_res, 'title': title, 'total_amount':total }
            return render(request,template_name,context)
        except:
            print("Unexpected error:", sys.exc_info())
            return render(request,template_name,context)
    return render(request,template_name,context)
# @login_required
# def check_receivables_year(request, year):
#     notices = Periodical_Notice.objects.filter(status=Notice_Status.ACTIVE, deadline__year=year)
#     context = {'notices': notices, 'year':year,'title':'%d年应收款'%(year)}
#     return render(request, 'receivables/check_receivables.html', context)

# @login_required
# def check_receivables_month(request, year, month):
#     notices = Periodical_Notice.objects.filter(status=Notice_Status.ACTIVE, deadline__year=year, deadline__month=month)
#     context = {'notices': notices, 'year':year, 'month':month, 'title':'%d年%d月应收款'%(year,month)}
#     return render(request, 'receivables/check_receivables.html', context)

