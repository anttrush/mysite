# Generated by Django 2.0.5 on 2018-10-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_id', models.IntegerField()),
                ('dev_name', models.CharField(max_length=100)),
                ('dev_score_Documentation', models.FloatField(default=0)),
                ('dev_score_CodeStyle', models.FloatField(default=0)),
                ('dev_score_Performance', models.FloatField(default=0)),
                ('dev_score_BestPractices', models.FloatField(default=0)),
                ('dev_score_Security', models.FloatField(default=0)),
                ('dev_score_Multithreading', models.FloatField(default=0)),
                ('dev_score_Design', models.FloatField(default=0)),
                ('dev_score_ErrorProne', models.FloatField(default=0)),
                ('dev_score_API1', models.FloatField(default=0)),
                ('dev_score_API2', models.FloatField(default=0)),
                ('dev_score_API3', models.FloatField(default=0)),
                ('dev_score_API4', models.FloatField(default=0)),
                ('dev_score_API5', models.FloatField(default=0)),
                ('dev_score_API6', models.FloatField(default=0)),
                ('dev_score_API7', models.FloatField(default=0)),
                ('dev_score_API8', models.FloatField(default=0)),
                ('dev_score_API9', models.FloatField(default=0)),
                ('dev_score_API10', models.FloatField(default=0)),
                ('dev_score_SolveIssue', models.IntegerField(default=0)),
                ('dev_score_Efficient', models.FloatField(default=0)),
                ('dev_follower_Number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_id', models.IntegerField()),
                ('proj_name', models.CharField(max_length=100)),
                ('proj_stars', models.IntegerField(default=0)),
                ('proj_owner', models.CharField(default='dont know yet', max_length=100)),
            ],
        ),
    ]
