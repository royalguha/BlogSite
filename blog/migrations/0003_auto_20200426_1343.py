# Generated by Django 2.1 on 2020-04-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='pics\\SUMIT_GUHA.jpg', upload_to='pics'),
        ),
    ]
