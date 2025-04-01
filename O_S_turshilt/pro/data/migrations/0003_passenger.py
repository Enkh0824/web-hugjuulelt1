# Generated by Django 5.1.7 on 2025-04-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_imformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=64)),
                ('firstname', models.CharField(max_length=64)),
                ('transports', models.ManyToManyField(blank=True, related_name='passengers', to='data.imformation')),
            ],
        ),
    ]
