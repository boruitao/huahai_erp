# Generated by Django 3.1.7 on 2021-04-11 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_auto_20210407_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.IntegerField(choices=[(0, 'Approved'), (1, 'Unapproved'), (2, 'Created'), (3, 'Annulled')], default=2),
        ),
    ]
