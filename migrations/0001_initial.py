# Generated by Django 3.2.9 on 2023-07-20 10:36

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work', '0002_work_unique_work'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opera',
            fields=[
                ('work_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='work.work')),
                ('language', models.CharField(blank=True, choices=[('cz', 'Czech'), ('da', 'Danish'), ('en', 'English'), ('fi', 'Finnish'), ('fr', 'French'), ('de', 'German'), ('hu', 'Hungarian'), ('it', 'Italian'), ('la', 'Latin'), ('po', 'Polish'), ('ru', 'Russian'), ('sa', 'Sanskrit'), ('es', 'Spanish'), ('sv', 'Swedish')], max_length=2)),
            ],
            bases=('work.work',),
            managers=[
                ('objects', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
    ]
