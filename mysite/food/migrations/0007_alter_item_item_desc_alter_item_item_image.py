# Generated by Django 4.2.5 on 2023-09-14 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_item_for_user_item_prod_code_alter_item_item_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_desc',
            field=models.CharField(default='Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando', max_length=500),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg', max_length=500),
        ),
    ]
