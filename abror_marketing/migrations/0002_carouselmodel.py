# Generated by Django 4.0.6 on 2022-07-18 12:28

import abror_marketing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abror_marketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=abror_marketing.models.upload_location)),
            ],
        ),
    ]
