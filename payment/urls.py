from django.conf.urls import url
from django.urls import path
from . import views
app_name = "payment"
urlpatterns = [
    #首次缴款单
    #TODO: payment_notices/first_payment_notice/ include history
    url(r'^payment_notices/first_payment_notice/active_payment_notices/$', views.active_first_payment_notices, name='active_first_payment_notices'),
    # url(r'^payment_notices/first_payment_notice/all/$', views.all_first_payment_notices, name='all_first_payment_notices'),
    url(r'^payment_notices/first_payment_notice/(?P<payment_notice_id>\d+)/$', views.check_first_payment_notice, name='check_first_payment_notice'),
    url(r'^payment_notices/first_payment_notice/approve/(?P<payment_notice_id>\d+)/$', views.approve_first_payment_notice, name='approve_first_payment_notice'),
    url(r'^payment_notices/first_payment_notice/edit/(?P<payment_notice_id>\d+)/$', views.edit_first_payment_notice, name='edit_first_payment_notice'),
    url(r'^payment_notices/first_payment_notice/print/(?P<payment_notice_id>\d+)/$', views.print_first_payment_notice, name='print_first_payment_notice'),
    url(r'^payment_notices/periodical_payment_notice/all/$', views.all_periodical_payment_notices, name='all_periodical_payment_notices'),
    url(r'^payment_notices/periodical_payment_notice/(?P<payment_notice_id>\d+)/$', views.check_periodical_payment_notice, name='check_periodical_payment_notice'),
    # url(r'^payment_notices/periodical_payment_notice/edit/(?P<payment_notice_id>\d+)/$', views.edit_periodical_payment_notice, name='edit_periodical_payment_notice'),
    # url(r'^payment_notices/periodical_payment_notice/print/(?P<payment_notice_id>\d+)/$', views.print_periodical_payment_notice, name='print_periodical_payment_notice'),
]