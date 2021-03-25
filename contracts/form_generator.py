from payment.models import First_Payment_Notice
from django.db import models
from .models import Contract, Company
from datetime import date
from dateutil.relativedelta import relativedelta

def generate_first_payment_notice(contract, num):
    rent = contract.monthly_price * contract.payment_cycle
    pf = contract.promotion_price
    pc = contract.payment_cycle
    tta = rent + pf
    sdate = contract.start_date
    edate = sdate + relativedelta(months=contract.payment_cycle) - relativedelta(days=1)
    ddl = sdate - relativedelta(days=15)
    today = date.today()
    nid = (today.year * 10000 + today.month * 100 + today.day) * 1000 + num

    payment_notice = First_Payment_Notice.create_notice(contract, ddl, sdate, edate, rent, 
    pc, pf, tta, nid, True, contract.buyer_company.company_name, contract.store_loc_code)

    return payment_notice

# def generate_periodical_payment_notice(contract, prev_edate, count):
#     count = 
#     rent = contract.monthly_price * contract.payment_cycle
#     pf = contract.promotion_price
#     pc = contract.payment_cycle
#     tta = rent + pf
#     sdate = contract.start_date
#     edate = sdate + relativedelta(months=contract.payment_cycle) - relativedelta(days=1)
#     ddl = sdate - relativedelta(days=15)
#     today = date.today()
#     nid = (today.year * 10000 + today.month * 100 + today.day) * 1000 + num

#     payment_notice = Payment_Notice.create_notice(contract, ddl, sdate, edate, rent, 
#     pc, pf, tta, nid, True, contract.company.company_name, contract.store_loc_code)

#     return payment_notice