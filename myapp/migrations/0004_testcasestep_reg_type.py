# Generated by Django 2.0.5 on 2018-05-27 09:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_testcasestep_element_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcasestep',
            name='reg_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=1024),
            preserve_default=False,
        ),
    ]
