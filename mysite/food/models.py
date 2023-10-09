from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(max_length=100, default='xyz')
    item_name = models.CharField(max_length=50)
    item_desc = models.CharField(max_length=500,default="Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando")
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg"
     )
    
    def __str__(self):
        return self.item_name