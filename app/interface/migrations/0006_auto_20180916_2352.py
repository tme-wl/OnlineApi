# Generated by Django 2.1.1 on 2018-09-16 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0005_auto_20180903_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='hostname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interface.HostName'),
        ),
    ]
