# Generated by Django 3.1.1 on 2020-10-11 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20201011_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.ImageField(upload_to=''),
        ),
    ]
