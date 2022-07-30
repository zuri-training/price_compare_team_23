from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from django.urls import reverse


# ************** Product Model ***********

# This model create how the product will be
# displayed to the customer with the needed
# information on the product(s)

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('smartphones', 'Smartphones'),
        ('laptops','Laptops'),
        ('desktop-computers','Desktop-computers'),
        ('television','Television'),
        ('smart-tvs','Smart-tvs'),
        ('digital-cameras','Digital-cameras'),
        ('generators','Generators')
    )
    id = models.UUIDField(default=uuid4,unique=True,primary_key=True)
    name = models.CharField(max_length=614)
    brand = models.CharField(max_length=256)
    img_src = models.CharField(max_length=614)


    #price = models.CharField(max_length=600)
    slug = models.SlugField(blank=True,max_length=124)
    category = models.CharField(max_length=32,choices=CATEGORY_CHOICES)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args,**kwargs)

    def get_absolute_url(self):
        #product_detail is the view
        return reverse("price_compare:product_detail", args=[
            self.id,
            self.slug
        ])
    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    username = models.CharField(max_length=614)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.username} on {self.product}'
