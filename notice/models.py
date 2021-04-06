from django.db import models

# Create your models here.
from contracts.models import Company, Contract
class PN_Status(models.IntegerChoices):
    ACTIVE = 0
    OVERDUE = 1
    PAYED = 2

class Notice(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField('deadline', null=True)
    payment_start_date = models.DateField('payment start date')
    payment_end_date = models.DateField('payment end date')
    notice_id = models.CharField(max_length=200)
    status = models.IntegerField(default=PN_Status.ACTIVE, choices=PN_Status.choices)
    cname = models.CharField(max_length=200,null=True)
    hname = models.CharField(max_length=200,null=True)
    hcity = models.CharField(max_length=200,null=True)
    loc_code = models.CharField(max_length=200,null=True)
    date_payed = models.DateField('date_payed', null=True)

    class Meta:
        abstract = True

class First_Notice(Notice):
    promotion_fee = models.DecimalField(max_digits=20, decimal_places=3,null=True)
    payment_cycle = models.IntegerField('payment cycle')
    total_rent = models.DecimalField(max_digits=20, decimal_places=3,null=True)
    total_amount = models.DecimalField(max_digits=20, decimal_places=3,null=True)
    date_released = models.DateField(auto_now_add=True)

    @classmethod
    def create_notice(cls, contract, ddl, start_date, end_date, rent, pc, pf, tta, nid, cname, loc, hname, hcity):
        payment_notice = cls(contract=contract, deadline=ddl, payment_start_date=start_date, payment_end_date=end_date, 
        notice_id=nid, total_rent=rent, payment_cycle=pc, promotion_fee=pf, total_amount=tta, cname=cname, 
        loc_code=loc, hname=hname, hcity=hcity)
        return payment_notice

class Periodical_Notice(Notice):
    total_amount = models.DecimalField(max_digits=20, decimal_places=3,null=True)
    period_num = models.IntegerField('period_num') # 季度
    date_released = models.DateField('date_released')

    @classmethod
    def create_notice(cls, contract, ddl, start_date, end_date, dr, tta, nid, cname, loc, pn, hname, hcity):
        payment_notice = cls(contract=contract, deadline=ddl, payment_start_date=start_date, payment_end_date=end_date, 
        date_released=dr, notice_id=nid, total_amount=tta, cname=cname, loc_code=loc, period_num=pn,
        hname=hname, hcity=hcity)
        return payment_notice