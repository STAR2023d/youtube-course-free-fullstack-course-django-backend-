from django.contrib import admin
from django.urls import include, path
from products.views import MakerListView, ProductCategoryListView, ProductsListView

app_name = "products"

urlpatterns = [
    path("", ProductsListView.as_view(), name="products-list"),
    path("categories", ProductCategoryListView.as_view(), name="category-list"),
    path("makers", MakerListView.as_view(), name="maker-list"),
]
