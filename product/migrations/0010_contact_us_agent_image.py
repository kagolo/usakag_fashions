# Generated by Django 4.0.3 on 2022-04-11 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_contact_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='agent_image',
            field=models.ImageField(default=0, upload_to='pic'),
            preserve_default=False,
        ),
    ]