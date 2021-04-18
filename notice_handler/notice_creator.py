from notice.models import First_Notice, Periodical_Notice
from django.db import models
from contracts.models import Contract, Company
from datetime import date
from dateutil.relativedelta import relativedelta

def generate_first_notice(contract, num):
    rent = contract.monthly_price * contract.payment_cycle
    pf = contract.promotion_price
    pc = contract.payment_cycle
    tta = rent + pf
    sdate = contract.start_date
    edate = sdate + relativedelta(months=contract.payment_cycle) - relativedelta(days=1)
    ddl = sdate - relativedelta(days=15)
    today = date.today()
    nid = (today.year * 10000 + today.month * 100 + today.day) * 1000 + num

    notice = First_Notice.create_notice(contract, ddl, sdate, edate, rent, 
    pc, pf, tta, nid, contract.buyer_company.company_name, contract.store_loc_code,
    contract.host_company.company_name, contract.host_company.city)
    notice.to_be_payed = tta
    notice.save()

def generate_periodical_notices(contract):
    #TODO: cover the case where number of dates are not exactly a full year
    payment_cycle = contract.payment_cycle
    sdate = contract.start_date
    edate = contract.end_date
    delta = relativedelta(edate, sdate)
    num_months = delta.months + delta.years * 12
    if delta.days > 0:
        num_months = num_months+1
    
    count_months = payment_cycle
    count = 2
    rent = contract.monthly_price * contract.payment_cycle
    while count_months < num_months:
        new_sdate = sdate + relativedelta(months=count_months)
        new_edate = sdate + relativedelta(months=(count_months+payment_cycle)) - relativedelta(days=1)
        count_months = count_months + payment_cycle
        if new_edate > edate:
            pp_notice = generate_pp_notice(contract, new_sdate, edate, rent, count)
            pp_notice.to_be_payed = rent
            pp_notice.save()
        else:
            pp_notice = generate_pp_notice(contract, new_sdate, new_edate, rent, count)
            pp_notice.to_be_payed = rent
            pp_notice.save()
        count = count + 1

def generate_pp_notice(contract, sdate, edate, total_amount, period_num):
    date_released = sdate - relativedelta(days=15)
    ddl = sdate
    nid = contract.contract_id + str(period_num)
    return Periodical_Notice.create_notice(contract, ddl, sdate, edate, date_released, 
    total_amount, nid, contract.buyer_company.company_name, contract.store_loc_code, period_num,
    contract.host_company.company_name, contract.host_company.city)