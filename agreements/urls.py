from django.conf.urls import url
from django.urls import path
from . import views
app_name = "agreements"
urlpatterns = [
    url(r'^agreements/search_contract/$', views.agreement_search_contract, name='agreement_search_contract'),
    url(r'^agreements/all/$', views.all_agreements, name='all_agreements'),
    url(r'^agreements/created/$', views.created_agreements, name='created_agreements'),
    url(r'^agreements/approved/$', views.approved_agreements, name='approved_agreements'),
    url(r'^agreements/unapproved/$', views.unapproved_agreements, name='unapproved_agreements'),
    url(r'^agreements/verify/$', views.verify_agreements, name='verify_agreements'),
 #   url(r'^agreements/verify/(?P<agreement_id>\d+)/$', views.verify_agreement, name='verify_agreement'),
    url(r'^agreements/(?P<agreement_id>\d+)/$', views.check_agreement, name='check_agreement'),
    url(r'^agreements/create_agreement/(?P<contract_id>\d+)/$', views.create_agreement, name='create_agreement'),
    url(r'^agreements/create_agreement/(?P<contract_id>\d+)/confirm/$', views.create_agreement_confirm, name='create_agreement_confirm'),
   # url(r'^agreements/create_first_pair/(?P<contract_id>\d+)/(?P<notice_id>\d+)/$', views.create_first_pair, name='create_first_pair'),
    url(r'^agreements/create_new_per_notice/(?P<contract_id>\d+)/(?P<notice_id>\d+)/$', views.create_new_per_notice, name='create_new_per_notice'),
    url(r'^agreements/create_per_pair/(?P<contract_id>\d+)/(?P<old_notice_id>\d+)/(?P<new_notice_id>\d+)/confirm/$', views.create_per_notice_pair_confirm, name='create_per_notice_pair_confirm'),
    url(r'^agreements/create_per_pair/(?P<contract_id>\d+)/(?P<old_notice_id>\d+)/(?P<new_notice_id>\d+)/$', views.create_per_notice_pair, name='create_per_notice_pair'),
    url(r'^agreements/delete_per_pair/(?P<contract_id>\d+)/(?P<new_notice_id>\d+)/$', views.delete_per_pair, name='delete_per_pair'),
]