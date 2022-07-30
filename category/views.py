from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from .models import Product 
from .scraper.jumia import get_jumia_product
from django.db.models import Q
from django.views.generic import ListView

#  ************product views*****************

#  takes into consideration:
#   @ Details about the product
#   @ Products Listing when potential customers make a search
#   @ Results of the search made by the customers

def product_detail(request,id,product):
    product = get_object_or_404(
        Product,
        slug=product,
        id = id,
    )


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'product/list.html'


class SearchResultView(ListView):
    model = Product
    template_name = 'product/search_result.html'
    context_object_name = 'products'
    def get_queryset(self):
        query = self.request.GET.get('search')
        list = Product.objects.filter(
            Q(name__icontains=query) | Q(brand__icontains=query)
        )
        return list
