# Generated by Django 3.1.6 on 2021-02-26 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyClubUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=60, verbose_name='zip code')),
                ('website', models.CharField(max_length=60, verbose_name='Website Adress')),
                ('phone_number', models.CharField(max_length=12, verbose_name='Contact number')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Event name')),
                ('event_date', models.DateField(verbose_name='Event date')),
                ('manager', models.CharField(max_length=60)),
                ('description', models.TextField(blank='True')),
                ('atendees', models.ManyToManyField(blank=True, to='Events.MyClubUser')),
                ('venue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Events.venue')),
            ],
        ),
    ]
