# Generated by Django 3.2.2 on 2021-05-12 23:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0003_alter_consulta_data_agendamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='data_agendamento',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 12, 23, 15, 53, 395666, tzinfo=utc), editable=False),
        ),
    ]
