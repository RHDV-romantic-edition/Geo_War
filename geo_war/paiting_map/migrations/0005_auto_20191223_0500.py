# Generated by Django 2.2.9 on 2019-12-23 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paiting_map', '0004_auto_20191223_0456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comand',
            name='Place',
            field=models.OneToOneField(blank=True, help_text='The team place in Scoreboard', null=True, on_delete=django.db.models.deletion.SET_NULL, to='paiting_map.Scoreboard'),
        ),
        migrations.AlterField(
            model_name='comand',
            name='black_squard',
            field=models.ManyToManyField(blank=True, help_text='The list of Squards that belongs to this project', to='paiting_map.Squard'),
        ),
    ]