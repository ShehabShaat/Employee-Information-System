# Generated by Django 4.1.7 on 2023-03-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='code',
            field=models.CharField(auto_created=True, blank=True, max_length=100),
        ),
    ]
