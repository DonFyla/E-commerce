# Generated by Django 4.1 on 2023-06-12 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0013_remove_product_category_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_desc',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
