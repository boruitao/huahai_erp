# Generated by Django 3.1.7 on 2021-03-30 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0008_contract_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='approved_by_manager',
        ),
    ]