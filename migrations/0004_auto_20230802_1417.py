# Generated by Django 3.2.9 on 2023-08-02 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operatick', '0003_delete_operaperformance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opera',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelManagers(
            name='opera',
            managers=[
            ],
        ),
    ]
