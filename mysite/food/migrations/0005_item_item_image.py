# Generated by Django 4.2.5 on 2023-09-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_remove_item_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://rrslide.com/wp-content/uploads/edd/2022/05/Food-Placeholder-Slides-PPT-14-min.jpg', max_length=500),
        ),
    ]