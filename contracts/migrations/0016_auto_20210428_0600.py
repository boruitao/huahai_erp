# Generated by Django 3.1.7 on 2021-04-28 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0015_auto_20210428_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=24000, max_digits=20),
            preserve_default=False,
        ),
    ]
