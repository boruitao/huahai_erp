from django.conf.urls import url
from django.urls import path
from . import views
app_name = "contracts"
urlpatterns = [
    path('', views.home, name='home'),
    # url(r'^companies/$', views.companies, name='companies'),
    # url(r'^new_company/$', views.new_company, name='new_company'),
    # url(r'^companies/(?P<company_id>\d+)/$', views.company, name='company'),
    # url(r'^contracts/$', views.contracts, name='contracts'),
    # url(r'^contracts/(?P<contract_id>\d+)/$', views.contract, name='contract'),
    # url(r'^new_contract/(?P<company_id>\d+)/$', views.new_contract, name='new_contract'),
]