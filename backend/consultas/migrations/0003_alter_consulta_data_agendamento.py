# Generated by Django 3.2.2 on 2021-05-12 22:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0002_auto_20210512_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 12, 22, 28, 40, 894061, tzinfo=utc), editable=False),
        ),
    ]