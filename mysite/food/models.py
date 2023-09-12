from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    item_desc = models.TextField(max_length=300)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500,
        default="https://rrslide.com/wp-content/uploads/edd/2022/05/Food-Placeholder-Slides-PPT-14-min.jpg"
    )

    def __str__(self):
        return self.item_name