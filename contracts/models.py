from django.db import models
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
import datetime
# Create your models here

class Contract_Status(models.IntegerChoices):
    CREATED = 0
    APPROVED = 1
    UNAPPROVED = 2
    COMPLETED = 3

#乙方
class Company(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    owner_name = models.CharField(max_length=200) # 姓名
    #owner_phone_num = PhoneNumberField(null=False, blank=False, unique=True) # 电话
    owner_address = models.CharField(max_length=2000) # 单位或家庭地址
    owner_id = models.CharField(max_length=200) # 身份证号
    company_name = models.CharField(max_length=2000) # 公司名
    core_business = models.CharField(max_length=2000) # 公司业务

#甲方
class Host(models.Model):
    company_name = models.CharField(max_length=2000) # 公司名
    owner_name = models.CharField(max_length=200) # 法人姓名
    #owner_phone_num = PhoneNumberField(null=False, blank=False, unique=True) # 电话
    address = models.CharField(max_length=2000) # 地址
    date_added = models.DateTimeField(auto_now_add=True)
    city = models.CharField(max_length=200) # 甲方公司所在城市

    def __str__(self):
        return self.company_name

class Contract(models.Model): #合同
    buyer_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    host_company = models.ForeignKey(Host, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_created') # 合同创建者
    approved_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='%(class)s_requests_approved',to_field='username', default='btao')
    status = models.IntegerField(default=Contract_Status.CREATED, choices=Contract_Status.choices) #状态
    date_added = models.DateTimeField(auto_now_add=True) #合同创建日期
    date_approved = models.DateTimeField('date_approved', null=True)
    date_completed = models.DateTimeField('date_completed', null=True)
    contract_id = models.CharField(default='无编号（未审核通过）', max_length=13) #合同编号
    start_date = models.DateField('start date') # 开始日期
    end_date = models.DateField('end date') # 截止日期
    sign_date = models.DateField('sign date') # 签订日期
    floor_num = models.IntegerField('floor number') # 楼层
    store_loc_code = models.CharField(max_length=200)# 铺位号
    region = models.CharField(max_length=200) # 铺位所在区
    unit_price = models.DecimalField(max_digits=20, decimal_places=2) # 单价
    area = models.DecimalField(max_digits=20, decimal_places=2) # 面积
    monthly_price = models.DecimalField(max_digits=20, decimal_places=2) # 月总价
    yearly_price = models.DecimalField(max_digits=20, decimal_places=2) # 全年总价
    total_price = models.DecimalField(max_digits=20, decimal_places=2) # 合同总价值
    to_be_payed = models.DecimalField(max_digits=20, decimal_places=2, null=True) # 还需支付的金额
    payment_cycle = models.IntegerField('payment cycle') # 收款周期按月计
    num_cycle = models.IntegerField('num of cycle') # 收款期数
    business = models.CharField(max_length=200) # 经营项目
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'), ('U', 'Unisex/Parody'))
    category = models.CharField(max_length=200,choices=GENDER_CHOICES) # 业态
    promotion_price = models.DecimalField(max_digits=20, decimal_places=2) # 推广费
    deposit = models.DecimalField(max_digits=20, decimal_places=2) # 铺位总定金
    perf_bond = models.DecimalField(max_digits=20, decimal_places=2) # 履约保证金总价
    water_bill = models.DecimalField(max_digits=20, decimal_places=2) # 每月单价水费
    elect_bill = models.DecimalField(max_digits=20, decimal_places=2) # 每月单价电费
