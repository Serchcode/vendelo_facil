from django.views.generic import View
from django.shortcuts import render
from .models import Product, Comment
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils.text import slugify
# Create your views here.


class ListViewProduct(View):
    def get(self, request, tag_slug=None):
        template_name = "products/list_products.html"
        products = Product.objects.all()
        tag = None
        if tag_slug:
            tag=get_object_or_404(Tag, slug=tag_slug)
            products = Product.filter(tags__in=[tag])
        context = {
            'products':products,
            'tag':tag,
        }
        return render(request,template_name,context)
