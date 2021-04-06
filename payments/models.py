from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from contracts.models import Company, Contract
from notice.models import First_Notice, Periodical_Notice

class Payment(models.Model):
    #contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    first_notice = models.ForeignKey(First_Notice, on_delete=models.CASCADE, related_name='%(class)s_first_notice', null=True)
    per_notice = models.ForeignKey(Periodical_Notice, on_delete=models.CASCADE, related_name='%(class)s_per_notice', null=True)

    is_first = models.BooleanField(default=False)
    is_per = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_received = models.DateField("date_received")
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    payment_id = models.CharField(max_length=200)
    cname = models.CharField(max_length=200)
    pay_method = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=20, decimal_places=3)
    reason = models.CharField(max_length=200)
