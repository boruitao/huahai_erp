# Generated by Django 3.1.7 on 2021-04-10 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_auto_20210407_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='first_notice',
            name='to_be_payed',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='periodical_notice',
            name='to_be_payed',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]