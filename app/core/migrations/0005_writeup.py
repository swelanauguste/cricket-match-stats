# Generated by Django 4.0.4 on 2022-04-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_sponsors_sponsor'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('team1', models.ImageField(upload_to='writeups_team1')),
                ('team2', models.ImageField(upload_to='writeups_team2')),
            ],
        ),
    ]