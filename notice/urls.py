from django.conf.urls import url
from django.urls import path
from . import views
app_name = "notice"
urlpatterns = [
    #首次缴款单
    #TODO: payment_notices/first_notice/ include history
    url(r'^notices/first_notice/all/$', views.all_first_notices, name='all_first_notices'),
    url(r'^notices/first_notice/(?P<notice_id>\d+)/$', views.check_first_notice, name='check_first_notice'),
    # url(r'^notices/first_notice/approve/(?P<notice_id>\d+)/$', views.approve_first_notice, name='approve_first_notice'),
    url(r'^notices/first_notice/edit/(?P<notice_id>\d+)/$', views.edit_first_notice, name='edit_first_notice'),
    url(r'^notices/first_notice/print/(?P<notice_id>\d+)/$', views.print_first_notice, name='print_first_notice'),
    url(r'^notices/periodical_notice/all/$', views.all_periodical_notices, name='all_periodical_notices'),
    url(r'^notices/periodical_notice/overdue/$', views.overdue_periodical_notices, name='overdue_periodical_notices'),
    url(r'^notices/periodical_notice/active/$', views.active_periodical_notices, name='active_periodical_notices'),
    url(r'^notices/periodical_notice/inactive/$', views.inactive_periodical_notices, name='inactive_periodical_notices'),
    url(r'^notices/periodical_notice/payed/$', views.payed_periodical_notices, name='payed_periodical_notices'),
    url(r'^notices/periodical_notice/(?P<notice_id>\d+)/$', views.check_periodical_notice, name='check_periodical_notice'),
    # url(r'^payment_notices/periodical_notice/edit/(?P<payment_notice_id>\d+)/$', views.edit_periodical_notice, name='edit_periodical_notice'),
    url(r'^notices/periodical_notice/print/(?P<notice_id>\d+)/$', views.print_periodical_notice, name='print_periodical_notice'),
]