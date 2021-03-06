# Generated by Django 3.1.7 on 2021-04-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0014_auto_20210407_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='num_cycle',
            field=models.IntegerField(default=4, verbose_name='num of cycle'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]
