# Generated by Django 5.1.2 on 2024-11-15 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_alter_blogmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog_images/'),
        ),
    ]
