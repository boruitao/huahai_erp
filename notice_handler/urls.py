from django.conf.urls import url
from django.urls import path
from . import views
app_name = "notice_handler"
urlpatterns = [
    url(r'^contracts/approve_contract/(?P<contract_id>\d+)/$', views.approve_contract, name='approve_contract'),
]