# Generated by Django 4.2.4 on 2023-08-28 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menu_image_alter_menu_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
