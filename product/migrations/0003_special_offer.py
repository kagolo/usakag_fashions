# Generated by Django 4.0.2 on 2022-02-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211028_0447'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=200)),
                ('item_image', models.ImageField(upload_to='pic')),
                ('item_price', models.CharField(max_length=200)),
                ('seller_name', models.CharField(max_length=200)),
                ('item_status', models.CharField(choices=[('USED', 'USED'), ('NEW', 'NEW')], max_length=100)),
            ],
        ),
    ]
