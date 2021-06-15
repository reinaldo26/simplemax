from django.db import models
from django.conf import settings
from PIL import Image
import os

class Product(models.Model):
    name = models.CharField(max_length=255)
    description_short = models.TextField(max_length=255)
    description_long = models.TextField()
    image = models.ImageField(upload_to='product_images/%Y/m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    price_marketing = models.FloatField()
    price_marketing_promo = models.FloatField(default=0)
    type = models.CharField(default='v', max_length=1, choices=(('v', 'variation '), ('s', 'simple')))

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        origin_width, original_height = img_pil.size

        if origin_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / origin_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(img_full_path, optimize=True, quality=50)
        

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        max_image_size = 800
        if self.image:
            self.resize_image(self.image, max_image_size)


    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models.FloatField()
    price_promo = models.FloatField(default=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.product.name

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
