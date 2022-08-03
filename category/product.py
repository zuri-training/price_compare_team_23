from category.models import Product
from category.scraper.jumia import get_jumia_products
from category.scraper.konga import konga_scraper_bot


def populatedB():
    list = get_jumia_products()
    for p in list:
        prd, created = Product.objects.get_or_create(name=p['name'],brand=p['brand'],category='smartphones',img_src=p['img_src'])
        # l = Product.objects.create(name=p['name'],brand=p['brand'],category='smartphones',img_src=p['img_src'])
        if created:
            prd.save()

def get_konga_product(product):
    list = konga_scraper_bot(product['name'])
    print(list)
