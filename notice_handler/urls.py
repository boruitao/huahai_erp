from django.conf.urls import url
from django.urls import path
from . import views
app_name = "notice_handler"
urlpatterns = [
    url(r'^contracts/verify/approve/(?P<contract_id>\d+)/$', views.approve_contract, name='approve_contract'),
    url(r'^contracts/verify/unapprove/(?P<contract_id>\d+)/$', views.unapprove_contract, name='unapprove_contract'),
    url(r'^contracts/manage/$', views.manage_search_contract, name='manage_search_contract'),
    url(r'^contracts/manage/check/(?P<contract_id>\d+)/$', views.manage_check_notices, name='manage_check_notices'),
    #url(r'^contracts/manage/modify/(?P<contract_id>\d+)/$', views.contract_manage_modify, name='contract_manage_modify'),
]