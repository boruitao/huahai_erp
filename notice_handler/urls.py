from django.conf.urls import url
from django.urls import path
from . import views
app_name = "notice_handler"
urlpatterns = [
    url(r'^contracts/verify/approve/(?P<contract_id>\d+)/$', views.approve_contract, name='approve_contract'),
    url(r'^contracts/verify/unapprove/(?P<contract_id>\d+)/$', views.unapprove_contract, name='unapprove_contract'),
    url(r'^payments/verify/approve/(?P<payment_id>\d+)/$', views.approve_payment, name='approve_payment'),
    url(r'^payments/verify/unapprove/(?P<payment_id>\d+)/$', views.unapprove_payment, name='unapprove_payment'),
    url(r'^agreements/verify/approve/(?P<agreement_id>\d+)/$', views.approve_agreement, name='approve_agreement'),
    url(r'^agreements/verify/unapprove/(?P<agreement_id>\d+)/$', views.unapprove_agreement, name='unapprove_agreement'),
    # url(r'^contracts/manage/$', views.manage_search_contract, name='manage_search_contract'),
    # url(r'^contracts/manage/check/(?P<contract_id>\d+)/$', views.manage_check_notices, name='manage_check_notices'),
    #url(r'^contracts/manage/modify/(?P<contract_id>\d+)/$', views.contract_manage_modify, name='contract_manage_modify'),
]