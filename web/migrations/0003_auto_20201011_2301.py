# Generated by Django 3.1.1 on 2020-10-11 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_project_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.ImageField(upload_to='web/images'),
        ),
    ]