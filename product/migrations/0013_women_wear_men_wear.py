# Generated by Django 4.0.4 on 2022-07-04 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_women_wear_men_wear'),
    ]

    operations = [
        migrations.AddField(
            model_name='women_wear',
            name='men_wear',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='product.men_wear'),
            preserve_default=False,
        ),
    ]