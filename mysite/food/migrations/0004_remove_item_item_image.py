# Generated by Django 4.2.5 on 2023-09-12 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_item_item_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_image',
        ),
    ]
