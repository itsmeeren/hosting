# Generated by Django 3.2.20 on 2023-12-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_imagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagemodel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
