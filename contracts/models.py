from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here
class Contract(models.model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING,default='')
    date_added = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField('start date') # 开始日期
    end_date = models.DateField('end date') # 截止日期
    sign_date = models.DateField('sign date') # 签订日期
    floor_num = models.IntegerField('floor number') # 楼层
    store_loc_code = models.CharField('store location code')# 铺位号
    region = models.CharField('region') # 铺位所在区
    unit_price = models.DecimalField('monthly unit price') # 单价
    area = models.DecimalField('area') # 面积
    monthly_price = models.DecimalField('monthly price') # 月总价
    yearly_price = models.DecimalField('yearly price') # 全年总价
    payment_cycle = models.IntegerField('payment cycle') # 收款周期按月计
    business = models.CharField('business') # 经营项目
    category = models.ChoiceField('business category') # 业态
    promotion_price = models.DecimalField('promotion price') # 推广费
    deposit = models.DecimalField('deposit') # 铺位总定金
    perf_bond = models.DecimalField('total performance bond') # 履约保证金总价
    water_bill = models.DecimalField('monthly water unit price') # 每月单价水费
    elect_bill = models.DecimalField('monthly electricity unit price') # 每月单价电费

class Company(models.model):
    date_added = models.DateTimeField(auto_now_add=True)
    owner_name = models.CharField('owner name') # 法人姓名
    owner_phone_num = PhoneNumberField(null=False, blank=False, unique=True) # 电话
    owner_address = models.CharField('owner address') # 单位或家庭地址
    owner_id = modles.CharField('owner id') # 身份证号
    company_name = models.CharField('company name') # 公司名
    core_business = models.CharField('core business') # 公司业务
