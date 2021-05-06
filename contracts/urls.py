from django.conf.urls import url
from django.urls import path
from . import views
app_name = "contracts"
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^companies/all_companies/$', views.all_companies, name='all_companies'),
    url(r'^companies/new_company/$', views.new_company, name='new_company'),
    url(r'^companies/(?P<company_id>\d+)/new_hosts/$', views.new_host, name='new_host'),
    url(r'^companies/(?P<company_id>\d+)/$', views.company, name='company'),
    url(r'^companies/(?P<company_id>\d+)/new_contract/$', views.new_contract, name='new_contract'),
    url(r'^contracts/all/$', views.all_contracts, name='all_contracts'),
    url(r'^contracts/created/$', views.created_contracts, name='created_contracts'),
    url(r'^contracts/approved/$', views.approved_contracts, name='approved_contracts'),
    url(r'^contracts/unapproved/$', views.unapproved_contracts, name='unapproved_contracts'),
    url(r'^contracts/completed/$', views.completed_contracts, name='completed_contracts'),
    url(r'^contracts/verify/$', views.verify_contracts, name='verify_contracts'),
    url(r'^contracts/verify/(?P<contract_id>\d+)/$', views.verify_contract, name='verify_contract'),
    #url(r'^contracts/approve_contract/(?P<contract_id>\d+)/$', views.approve_contract, name='approve_contract'),
    url(r'^contracts/check/(?P<contract_id>\d+)/$', views.check_contract, name='check_contract'),
    url(r'^contracts/search/(?P<status_id>\d+)/$', views.search_contracts, name='search_contracts'),
]