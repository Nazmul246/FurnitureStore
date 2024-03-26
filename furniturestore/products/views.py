from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from django.views import View
from .models import *


def home(request):
    return HttpResponse("Welcome to our e-commerce website!")


class CategoryProductsView(View):
    def get(self, request):
        sofa_category = Category.objects.get(name='sofa')
        sofa_products = Product.objects.filter(category=sofa_category)
        product_names = ', '.join(product.name for product in sofa_products)
        return HttpResponse(f"Products in the 'sofa' category: {product_names}")
    
class EachCategoryProductsView(View):
    def get(self, request, category_name):
        try:
            category = Category.objects.get(name=category_name)
        except Category.DoesNotExist:
            return HttpResponse(f"Category '{category_name}' does not exist.", status=404)
        category_products = Product.objects.filter(category=category)
        product_names = ', '.join(product.name for product in category_products)

        return HttpResponse(f"Products in the '{category_name}' category: {product_names}")


class HomeSolutionView(View):
    def get(self, request):
        home_product=Product.objects.filter(subcategory='home')
        product_names = ', '.join(product.name for product in home_product)
        return HttpResponse(f"Products in the 'sofa' category: {product_names}")
        
class OfficeSolutionView(View):
    def get(self, request):
        office_product=Product.objects.filter(subcategory='office')
        product_names = ', '.join(product.name for product in office_product)
        return HttpResponse(f"Products in the 'sofa' category: {product_names}")

class DetailProductView(View):
    def get(self, request, id):
        product = Product.objects.filter(id = id)
        return HttpResponse(f"Products in the 'sofa' category: {product}")