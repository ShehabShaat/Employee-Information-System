# Generated by Django 4.1.7 on 2023-03-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_employees_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='code',
            field=models.IntegerField(auto_created=True),
        ),
    ]
