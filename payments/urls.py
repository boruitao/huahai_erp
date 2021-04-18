from django.conf.urls import url
from django.urls import path
from . import views
app_name = "payments"
urlpatterns = [
    #首次收款单
    url(r'^payments/search_contract/$', views.payment_search_contract, name='payment_search_contract'),
    url(r'^payments/check_notices/(?P<contract_id>\d+)/$', views.payment_check_notices, name='payment_check_notices'),
    url(r'^payments/verify_payments/(?P<payment_id>\d+)/$', views.verify_single_payment, name='verify_single_payment'),
    url(r'^payments/verify_payments/$', views.verify_payments, name='verify_payments'),
    url(r'^payments/all/$', views.all_payments, name='all_payments'),
    #url(r'^payment/confirm_payment/(?P<payment_id>\d+)/$', views.confirm_payment, name='confirm_payment'),
    url(r'^payments/create_payment/(?P<notice_id>\d+)/(?P<is_first>\d+)/$', views.create_payment, name='create_payment'),
   # url(r'^payment/create_payment/periodical/(?P<notice_id>\d+)/<int:is_first>/$', views.create_periodical_payment, name='create_periodical_payment'),
]