# Generated by Django 3.1.7 on 2021-03-23 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0004_auto_20210322_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='host_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contracts.host'),
        ),
    ]
