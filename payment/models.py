from django.db import models

# Create your models here.
from contracts.models import Company, Contract

class Payment_Notice(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_released = models.DateField(auto_now_add=True)
    deadline = models.DateField('deadline', null=True)
    payment_start_date = models.DateField('payment start date')
    payment_end_date = models.DateField('payment end date')
    notice_id = models.CharField(max_length=200)
    is_active = models.BooleanField(default=False)
    cname = models.CharField(max_length=200,null=True)
    loc_code = models.CharField(max_length=200,null=True)

    class Meta:
        abstract = True

class First_Payment_Notice(Payment_Notice):
    promotion_fee = models.DecimalField(max_digits=20, decimal_places=3,null=True)
    payment_cycle = models.IntegerField('payment cycle')
    total_rent = models.DecimalField(max_digits=20, decimal_places=3,null=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=3,null=True)

    @classmethod
    def create_notice(cls, contract, ddl, start_date, end_date, rent, pc, pf, tta, nid, is_active, cname, loc):
        payment_notice = cls(contract=contract, deadline=ddl, payment_start_date=start_date, payment_end_date=end_date, 
        notice_id=nid, total_rent=rent, payment_cycle=pc, promotion_fee=pf, total_amount=tta, is_active=True, cname=cname, loc_code=loc)
        return payment_notice

class Periodical_Payment_Notice(Payment_Notice):
    total_amount = models.DecimalField(max_digits=20, decimal_places=3,null=True)
    period_num = models.IntegerField('period_num') # 季度
    
    @classmethod
    def create_notice(cls, contract, ddl, start_date, end_date, tta, nid, is_active, cname, loc):
        payment_notice = cls(contract=contract, deadline=ddl, payment_start_date=start_date, payment_end_date=end_date, 
        notice_id=nid, total_amount=tta, is_active=True, cname=cname, loc_code=loc)
        return payment_notice