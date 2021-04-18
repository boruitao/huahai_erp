from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from contracts.models import Company, Contract
from notice.models import Notice, First_Notice, Periodical_Notice

class Agreement(models.Model):
    old_contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='%(class)s_old')
    new_contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='%(class)s_new')

    date_added = models.DateTimeField(auto_now_add=True)    
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_created')
    approved_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_approved')
    text = models.CharField(max_length=200)

class Notice_Pair(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    old_first_notice = models.ForeignKey(First_Notice, on_delete=models.DO_NOTHING, related_name='%(class)s_old_f', null=True)
    new_first_notice = models.ForeignKey(First_Notice, on_delete=models.DO_NOTHING, related_name='%(class)s_new_f', null=True)
    old_per_notice = models.ForeignKey(Periodical_Notice, on_delete=models.DO_NOTHING, related_name='%(class)s_old_p', null=True)
    new_per_notice = models.ForeignKey(Periodical_Notice, on_delete=models.DO_NOTHING, related_name='%(class)s_new_p', null=True)
