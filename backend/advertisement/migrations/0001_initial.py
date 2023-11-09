# Generated by Django 4.2.5 on 2023-11-09 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='ads/')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('target_location', models.CharField(blank=True, max_length=100, null=True)),
                ('target_user_type', models.CharField(choices=[('all', 'All Users'), ('escort', 'Escorts'), ('client', 'Clients')], default='all', max_length=50)),
                ('clicks', models.IntegerField(default=0)),
                ('impressions', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
