# Generated by Django 2.2.1 on 2019-06-13 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0007_auto_20190613_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='data_de_entrada_no_brasil',
            field=models.DateField(blank=True, null=True),
        ),
    ]