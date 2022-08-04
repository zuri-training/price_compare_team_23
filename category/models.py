from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from django.urls import reverse
from django.contrib.auth.models import User


# ************** Product Model ***********

# This model create how the product will be
# displayed to the customer with the needed
# information on the product(s)


class Product(models.Model):
    CATEGORY_CHOICES = (
        ("smartphones", "Smartphones"),
        ("laptops", "Laptops"),
        ("desktop-computers", "Desktop-computers"),
        ("television", "Television"),
        ("smart-tvs", "Smart-tvs"),
        ("digital-cameras", "Digital-cameras"),
        ("generators", "Generators"),
    )

    RAM_SIZES = (
        ("2gb","2GB"),
        ("4gb","4GB"),
        ("6gb","6GB"),
        ("8gb","8GB"),
    )

    ROM_SIZES = (
        ("16gb","16GB"),
        ("32gb","32GB"),
        ("64gb","64GB"),
        ("128gb","128GB"),
        ("256gb","256GB"),
    )

    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=256)
    image_src = models.CharField(max_length=614)
    rom_size = models.CharField(max_length=10, choices=ROM_SIZES)
    ram_size = models.CharField(max_length=10, choices=RAM_SIZES)

    # should just be called brand
    # properties=models.CharField(max_length=300,null=True)
    # category = models.CharField(max_length=256)
    # we wouldn't need to store the vendor name since we get this from the query in the detail view
    # vendor=models.CharField(max_length=100, null=True)
    # we get the price directly from the store
    # price = models.CharField(max_length=600, null=True)
    slug = models.SlugField(blank=True, max_length=255)
    category = models.CharField(max_length=64, choices=CATEGORY_CHOICES)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # product_detail is the view
        return reverse("category:product_detail", args=[self.id, self.slug])

    def __str__(self):
        return self.name


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments"
    )
    username = models.CharField(max_length=614)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ("created",)

    def __str__(self):
        return f"Comment by {self.username} on {self.product}"
