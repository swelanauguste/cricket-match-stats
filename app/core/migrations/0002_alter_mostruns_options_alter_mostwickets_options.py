# Generated by Django 4.0.4 on 2022-04-28 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mostruns',
            options={'verbose_name_plural': 'Most Runs'},
        ),
        migrations.AlterModelOptions(
            name='mostwickets',
            options={'verbose_name_plural': 'Most Wickets'},
        ),
    ]