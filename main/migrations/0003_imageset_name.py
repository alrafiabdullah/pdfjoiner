# Generated by Django 3.1.1 on 2020-09-23 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200922_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageset',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
