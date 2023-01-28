import datetime

from django.db import models


class Group(models.Model):
    name_group = models.CharField(max_length=50, verbose_name='Group name', db_column='g_name')
    start_date = models.DateField(default=datetime.date.today)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'groups'

