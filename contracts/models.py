from django.db import models
import datetime
# Create your models here.
class Contract(models.model):
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    floor_num = models.IntegerField('floor number') # 楼层
    store_loc_code = models.CharField('store location code')# 铺位号
    unit_price = models.DecimalField('unit price') # 单价
    

