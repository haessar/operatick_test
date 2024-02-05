# Generated by Django 3.2.9 on 2024-02-05 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operatick', '0005_alter_opera_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opera',
            name='language',
            field=models.CharField(blank=True, choices=[('hy', 'Armenian'), ('cz', 'Czech'), ('da', 'Danish'), ('nl', 'Dutch'), ('en', 'English'), ('fi', 'Finnish'), ('fr', 'French'), ('de', 'German'), ('hu', 'Hungarian'), ('it', 'Italian'), ('la', 'Latin'), ('lt', 'Lithuanian'), ('po', 'Polish'), ('ru', 'Russian'), ('sa', 'Sanskrit'), ('es', 'Spanish'), ('sv', 'Swedish')], max_length=2),
        ),
    ]
