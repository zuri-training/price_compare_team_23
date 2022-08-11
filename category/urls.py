from django.urls import path
from . import views
from .views import ProductListView, product_detail, SearchResultView


app_name = "category"

urlpatterns = [
    path("product", ProductListView.as_view(), name="landing"),
    path("<uuid:id>/<slug:product>", product_detail, name="product_detail"),
    path("search/", SearchResultView.as_view(), name="search_results"),
    path("", views.index_view, name="home"),
    path("faq", views.faq_view, name="faq"),
    path("contact", views.contact_page, name="contact_page"),
    path("privacy", views.privacy, name="privacy"),
    path("terms_of_service", views.terms_of_service, name="terms_of_service"),
    path("documentation", views.documentation, name="documentation"),
]
