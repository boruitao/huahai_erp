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
    url(r'^contracts/all_contracts/$', views.all_contracts, name='all_contracts'),
    url(r'^contracts/all_created_contracts/$', views.all_created_contracts, name='all_created_contracts'),
    url(r'^contracts/all_approved_contracts/$', views.all_approved_contracts, name='all_approved_contracts'),
    url(r'^contracts/all_unapproved_contracts/$', views.all_unapproved_contracts, name='all_unapproved_contracts'),
    url(r'^contracts/all_completed_contracts/$', views.all_completed_contracts, name='all_completed_contracts'),
    url(r'^contracts/verify_contracts/$', views.verify_contracts, name='verify_contracts'),
    #url(r'^contracts/approve_contract/(?P<contract_id>\d+)/$', views.approve_contract, name='approve_contract'),
    url(r'^contracts/check/(?P<contract_id>\d+)/$', views.check_contract, name='check_contract'),
    url(r'^contracts/search/(?P<status_id>\d+)/$', views.search_contracts, name='search_contracts'),
]