# Generated by Django 3.0.3 on 2020-06-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200604_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='bagicapidata',
            name='news_coverImage',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='bagicapidata',
            name='news_datePublished',
            field=models.CharField(max_length=20),
        ),
    ]
