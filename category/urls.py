from django.urls import path
from .views import ProductListView , product_detail , SearchResultView,user_search

app_name = 'category'

urlpatterns = [
    path('search',user_search, name='search'),
    path('',ProductListView.as_view(), name='landing'),
    path('<uuid:id>/<slug:product>',product_detail, name='product_detail'),
    path('search/',SearchResultView.as_view(),name = 'search_results'),
    ]   