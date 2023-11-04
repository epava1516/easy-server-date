# Generated by Django 4.2.5 on 2023-11-04 14:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escortavailability',
            name='day_of_week',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.RemoveField(
            model_name='escortimage',
            name='escort_profile',
        ),
        migrations.RemoveField(
            model_name='escortprofiletag',
            name='escort_profile',
        ),
        migrations.AddField(
            model_name='escortimage',
            name='escort_profile',
            field=models.ManyToManyField(related_name='images', to='eprofile.escortprofile'),
        ),
        migrations.AddField(
            model_name='escortprofiletag',
            name='escort_profile',
            field=models.ManyToManyField(related_name='tags', to='eprofile.escortprofile'),
        ),
    ]