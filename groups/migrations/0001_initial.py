# Generated by Django 4.1.5 on 2023-01-28 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_group', models.CharField(db_column='g_name', max_length=50, verbose_name='Group name')),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
    ]