# Generated by Django 5.1 on 2024-08-22 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_alter_employee_addressdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='projects',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='qualifications',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='workExperience',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
