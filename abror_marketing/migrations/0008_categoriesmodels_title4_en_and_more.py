# Generated by Django 4.0.6 on 2022-07-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abror_marketing', '0007_rename_title_categoriesmodels_title1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoriesmodels',
            name='title4_en',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='categoriesmodels',
            name='title4_ru',
            field=models.CharField(max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='categoriesmodels',
            name='title4_uz',
            field=models.CharField(max_length=55, null=True),
        ),
    ]