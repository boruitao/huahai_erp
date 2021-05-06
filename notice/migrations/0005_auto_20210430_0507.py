# Generated by Django 3.1.7 on 2021-04-30 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0004_auto_20210428_0427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first_notice',
            name='status',
            field=models.IntegerField(choices=[(0, 'Active'), (1, 'Overdue'), (2, 'Payed'), (3, 'Inactive'), (4, 'Tmp')], default=0),
        ),
        migrations.AlterField(
            model_name='periodical_notice',
            name='status',
            field=models.IntegerField(choices=[(0, 'Active'), (1, 'Overdue'), (2, 'Payed'), (3, 'Inactive'), (4, 'Tmp')], default=0),
        ),
    ]
