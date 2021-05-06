# Generated by Django 3.1.7 on 2021-04-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0016_auto_20210428_0600'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='date_completed',
            field=models.DateTimeField(null=True, verbose_name='date_completed'),
        ),
        migrations.AddField(
            model_name='contract',
            name='to_be_payed',
            field=models.DecimalField(decimal_places=2, default=12000, max_digits=20),
            preserve_default=False,
        ),
    ]