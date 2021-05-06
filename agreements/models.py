from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from contracts.models import Company, Contract
from notice.models import Notice, First_Notice, Periodical_Notice
# add time or reduce payment
class Agreement_Status(models.IntegerChoices):
    CREATED = 0
    APPROVED = 1
    UNAPPROVED = 2

class Agreement(models.Model):
    old_contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='%(class)s_old')
    new_contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='%(class)s_new', null=True)
    status = models.IntegerField(default=Agreement_Status.CREATED, choices=Agreement_Status.choices) #状态

    date_added = models.DateTimeField(auto_now_add=True)    
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_created')
    approved_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_approved', null=True)
    reason = models.CharField(max_length=200)
    cname = models.CharField(max_length=200)

class Per_Notice_Pair(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    old_notice = models.ForeignKey(Periodical_Notice, on_delete=models.DO_NOTHING, related_name='%(class)s_old_p', null=True)
    new_notice = models.ForeignKey(Periodical_Notice, on_delete=models.DO_NOTHING, related_name='%(class)s_new_p', null=True)

    @classmethod
    def create_pair(cls, old_notice, new_notice):
        pair = cls(old_notice=old_notice, new_notice=new_notice)
        return pair

class First_Notice_Pair(models.Model):
    agreement = models.ForeignKey(Agreement, on_delete=models.CASCADE, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    old_notice = models.ForeignKey(First_Notice, on_delete=models.DO_NOTHING, related_name='%(class)s_old_f', null=True)
    new_notice = models.ForeignKey(First_Notice, on_delete=models.DO_NOTHING, related_name='%(class)s_new_f', null=True)

    @classmethod
    def create_pair(cls, old_notice, new_notice):
        pair = cls(old_notice=old_notice, new_notice=new_notice)
        return pair