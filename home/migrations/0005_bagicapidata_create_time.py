# Generated by Django 3.0.3 on 2020-06-04 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200604_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='bagicapidata',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
