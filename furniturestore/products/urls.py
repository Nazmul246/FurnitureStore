from django.urls import path
from .views import *


urlpatterns = [
    path('category/', CategoryProductsView.as_view(), name='category_products'),
    path('category/<str:category_name>/', EachCategoryProductsView.as_view(), name='each_category_products'),
    path('home-solution/', HomeSolutionView.as_view(), name='home_solution'),
    path('office-solution/', OfficeSolutionView.as_view(), name='office_solution'),
    path('product-details/<int:id>/', DetailProductView.as_view(), name='detail_product_view'),

]