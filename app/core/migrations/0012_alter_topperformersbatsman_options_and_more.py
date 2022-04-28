# Generated by Django 4.0.4 on 2022-04-28 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_topperformersbatsman_innings_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topperformersbatsman',
            options={'ordering': ('-runs',), 'verbose_name_plural': 'Top Performers Batsmen'},
        ),
        migrations.AlterModelOptions(
            name='topperformersbowler',
            options={'ordering': ('-wickets',), 'verbose_name_plural': 'Top Performers Bowlers'},
        ),
        migrations.AlterField(
            model_name='topperformersbowler',
            name='overs',
            field=models.IntegerField(),
        ),
    ]