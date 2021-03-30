# Generated by Django 3.1.7 on 2021-03-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0009_remove_contract_approved_by_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='status',
            field=models.IntegerField(choices=[(0, 'Created'), (1, 'Approved'), (2, 'Unapproved'), (3, 'Completed')], default=0),
        ),
    ]
