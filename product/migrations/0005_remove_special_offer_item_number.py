# Generated by Django 4.0.2 on 2022-02-22 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_special_offer_item_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='special_offer',
            name='item_number',
        ),
    ]
