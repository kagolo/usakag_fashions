# Generated by Django 4.0.2 on 2022-02-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_special_offer_item_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_number', models.CharField(max_length=200, unique=True)),
                ('item_name', models.CharField(max_length=200)),
                ('item_image', models.ImageField(upload_to='pic')),
                ('item_price1', models.CharField(max_length=200)),
                ('item_price2', models.CharField(max_length=200)),
                ('item_status', models.CharField(choices=[('USED', 'USED'), ('NEW', 'NEW')], max_length=100)),
                ('seller_name', models.CharField(max_length=200)),
            ],
        ),
    ]