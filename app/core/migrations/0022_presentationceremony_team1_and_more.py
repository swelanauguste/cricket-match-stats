# Generated by Django 4.0.4 on 2022-05-02 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_presentationceremony'),
    ]

    operations = [
        migrations.AddField(
            model_name='presentationceremony',
            name='team1',
            field=models.ImageField(blank=True, null=True, upload_to='presentation_team3'),
        ),
        migrations.AddField(
            model_name='presentationceremony',
            name='team2',
            field=models.ImageField(blank=True, null=True, upload_to='presentation_team3'),
        ),
        migrations.AddField(
            model_name='presentationceremony',
            name='team3',
            field=models.ImageField(blank=True, null=True, upload_to='presentation_team3'),
        ),
    ]
