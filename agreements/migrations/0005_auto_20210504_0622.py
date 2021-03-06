# Generated by Django 3.1.7 on 2021-05-04 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agreements', '0004_auto_20210430_0543'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='cname',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agreement',
            name='status',
            field=models.IntegerField(choices=[(0, 'Created'), (1, 'Approved'), (2, 'Unapproved')], default=0),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='approved_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='agreement_requests_approved', to=settings.AUTH_USER_MODEL),
        ),
    ]
