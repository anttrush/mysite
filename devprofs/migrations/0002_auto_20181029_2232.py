# Generated by Django 2.0.5 on 2018-10-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devprofs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proj_owner',
            field=models.IntegerField(),
        ),
    ]
