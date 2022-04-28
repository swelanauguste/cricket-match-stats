# Generated by Django 4.0.4 on 2022-04-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_topperformersbatsman_team_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topperformersbowler',
            options={'ordering': ('runs',), 'verbose_name_plural': 'Top Performers Bowlers'},
        ),
        migrations.AlterField(
            model_name='topperformersbowler',
            name='overs',
            field=models.IntegerField(default=0),
        ),
    ]