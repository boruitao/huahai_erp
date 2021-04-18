from django.conf.urls import url
from django.urls import path
from . import views
app_name = "worksheet"
urlpatterns = [
    path('worksheet/receivables/', views.check_receivables, name='check_receivables'),
    path('worksheet/receivables/search/', views.search_receivables_notices, name='search_receivables_notices'),
    #path('worksheet/receivables/<int:year>/', views.check_receivables_year, name='check_receivables_year'),
    #path('worksheet/receivables/<int:year>/<int:month>/', views.check_receivables_month, name='check_receivables_month'),
    path('worksheet/overdue/', views.check_overdue, name='check_overdue'),
    path('worksheet/overdue/search/', views.search_overdue_notices, name='search_overdue_notices'),
    # path(r'^worksheet/general/$', views.check_general, name='check_general'),
]