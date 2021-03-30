from django.conf.urls import url
from django.urls import path
from . import views
app_name = "notice_handler"
urlpatterns = [
    url(r'^approve_contract/(?P<contract_id>\d+)/$', views.approve_contract, name='approve_contract'),
    url(r'^contracts/manage/$', views.contract_manage_search, name='contract_manage_search'),
    url(r'^contracts/manage/check/(?P<contract_id>\d+)/$', views.contract_manage_check, name='contract_manage_check'),
    #url(r'^contracts/manage/modify/(?P<contract_id>\d+)/$', views.contract_manage_modify, name='contract_manage_modify'),
]