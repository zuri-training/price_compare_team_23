from category.models import Product
from category.scraper.jumia import get_jumia_products
from category.scraper.konga import konga_scraper_bot


def populatedB():
    list = get_jumia_products()
    for p in list:
        prd, created = Product.objects.get_or_create(
            name=p["name"],
            brand=p["brand"],
            category="smartphones",
            image_src=p["image_src"],
        )
        # l = Product.objects.create(name=p['name'],brand=p['brand'],category='smartphones',img_src=p['img_src'])
        if created:
            prd.save()


def get_konga_products(product_name):
    _products = [
        {
            "name": "Samsung Galaxy S22 ultra",
            "brand": "Samsung",
            "category": "smartphones",
            "link": "https://www.konga.com/product/samsung-s22-ultra-12gb-ram-256gb-rom-dual-sim-blue-5807738",
            "price": "₦827,500",
            "platform_name": "Konga",
        },
    ]
