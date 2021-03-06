# Generated by Django 3.1.7 on 2021-04-30 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0005_auto_20210430_0507'),
        ('agreements', '0002_auto_20210429_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='First_Notice_Pair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('agreement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agreements.agreement')),
                ('new_notice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='first_notice_pair_new_f', to='notice.first_notice')),
                ('old_notice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='first_notice_pair_old_f', to='notice.first_notice')),
            ],
        ),
        migrations.CreateModel(
            name='Per_Notice_Pair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('agreement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agreements.agreement')),
                ('new_notice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='per_notice_pair_new_p', to='notice.periodical_notice')),
                ('old_notice', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='per_notice_pair_old_p', to='notice.periodical_notice')),
            ],
        ),
        migrations.DeleteModel(
            name='Notice_Pair',
        ),
    ]
