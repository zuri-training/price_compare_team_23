from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, FileResponse
from .models import Comment, Product
from .scraper.jumia import get_jumia_product
from django.db.models import Q
from django.views.generic import ListView
from .product import populatedB
from .products import get_ali_express_product, get_product_konga

# import schedule

#  ************product views*****************

#  takes into consideration:
#   @ Details about the product
#   @ Products Listing when potential customers make a search
#   @ Results of the search made by the customers


def faq_view(request):
    return render(request, "category/faq.html")


def privacy(request):
    return render(request, "category/privacy.html")


def terms_of_service(request):
    return render(request, "category/terms_of_service.html")


def documentation(request):
    return render(request, "category/documentation.html")


def user_guide_pdf(response):
    return FileResponse(
        open("pdf/user_guide.pdf", "rb"),
        as_attachment=True,
        content_type="application/pdf",
    )


def index_view(request):
    products = Product.objects.all()[1:7]
    top = Product.objects.all()[0:1]
    context = {"products": products, "top": top}
    return render(request, "category/index.html", context)


def contact_page(request):
    return render(request, "category/contact.html")


def about_page(request):
    return render(request, "category/about.html")


def product_detail(request, id, product):
    product = get_object_or_404(
        Product,
        slug=product,
        id=id,
    )

    comments = product.comments.filter(active=True)
    new_comment = None
    prd = {
        "name": product.name,
        "brand": product.brand,
    }
    specs = {
        "ram_size": product.ram_size,
        "rom_size": product.rom_size,
    }
    platforms = []
    print(get_product_konga(prd["name"]))
    platforms.append(get_product_konga(prd["name"]))

    if request.method == "POST":
        # A comment was posted
        comment_body = request.POST["body"]
        if comment_body != None or comment_body != "":
            # Create Comment object but don't save to database yet
            new_comment = Comment(body=comment_body)
            # Assign the current post to the comment
            new_comment.product = product
            new_comment.username = request.user.username
            new_comment.save()
            return HttpResponseRedirect(
                f"{product.slug}",
                {
                    "product": product,
                    "comments": comments,
                    "platforms": platforms,
                    "new_comment": new_comment,
                    "specs": specs,
                },
            )

    return render(
        request,
        "category/product-details.html",
        {
            "product": product,
            "comments": comments,
            "platforms": platforms,
            "new_comment": new_comment,
            "specs": specs,
        },
    )


class ProductListView(ListView):
    model = Product
    # populatedB()
    context_object_name = "products"
    template_name = "category/product_page.html"


class SearchResultView(ListView):
    model = Product
    template_name = "category/result.html"
    context_object_name = "products"

    def get_queryset(self):
        query = self.request.GET.get("search")
        list = Product.objects.filter(
            Q(name__icontains=query) | Q(brand__icontains=query)
        )
        return list
