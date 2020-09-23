# Generated by Django 3.1.1 on 2020-09-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_imageset_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageset',
            name='image',
        ),
        migrations.RemoveField(
            model_name='imageset',
            name='name',
        ),
        migrations.AddField(
            model_name='imageset',
            name='pdf_file',
            field=models.FileField(default='', upload_to='pdfs/'),
            preserve_default=False,
        ),
    ]