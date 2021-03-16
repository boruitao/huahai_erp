from django.conf.urls import url
from django.urls import path
from . import views
app_name = "payment"
urlpatterns = [
    url(r'^payment_notices/active_payment_notices/$', views.active_payment_notices, name='active_payment_notices'),
    url(r'^payment_notices/(?P<payment_notice_id>\d+)/$', views.check_payment_notice, name='check_payment_notice'),
]