# Generated by Django 2.2.9 on 2019-12-23 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiting_map', '0005_auto_20191223_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squard',
            name='word_1',
            field=models.CharField(help_text='Word 1', max_length=100),
        ),
    ]