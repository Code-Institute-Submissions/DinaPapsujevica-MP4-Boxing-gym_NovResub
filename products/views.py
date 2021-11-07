import os
import json
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse

from home.views import handle_uploaded_file, build_image_url
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from boxing_gym.verify_request import verify_request


@verify_request
@login_required
@user_passes_test(lambda user: user.is_superuser)
def add_product(request):
    context = {}
    user = User.objects.get(id=request.user.id)
    form = ProductForm()
    if request.method == 'POST':
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']
        image_link = request.FILES.get('image_link')
        data['image_link'] = request.FILES.get('image_link')
        data['user_id'] = request.user.id
        product = Product.objects.create(**data)
        print("is_uploaded: ",image_link)
        isupload = handle_uploaded_file(image_link)
        return HttpResponseRedirect('/products')
    context['form'] = form
    return render(request, "products/add_product.html", context)


@verify_request
def view_products(request):
    products = Product.objects.all()
    has_item = len(products) == 0 and request.user.is_superuser
    print("has_item", has_item)
    product_data = []
    for product in products:
        product_data.append({
            'image': build_image_url(product.image_link.url),
            'name': product.name,
            'id': product.id,
            'price': float(product.price),
            'description': product.description,
            'sku': product.sku
        })
    return render(request, 'products/products.html', {'products': product_data, 'has_item': has_item})


@verify_request
@login_required
def product_detail(request, product_id):
    product = Product.objects.get(id=int(product_id))
    product.image_link = build_image_url(product.image_link.url)
    return render(request, 'products/product_detail.html', {'product': product})


@verify_request
@login_required
@user_passes_test(lambda user: user.is_superuser)
def edit_product(request, product_id):
    product_data = Product.objects.get(id=int(product_id))
    if request.method == 'POST':
        category = request.POST.get('category')
        name = request.POST.get('name')
        image_link = request.FILES.get('image_link', None)
        sku = request.POST.get('sku')
        price = request.POST.get('price')
        description = request.POST.get('description')
        sizes = request.POST.get('sizes')
        data = dict(name=name, image_link=image_link, sku=sku,
                    description=description, sizes=sizes, price=float(price))
        print("data:", data)
        product_data.category = category
        product_data.name = name
        if image_link is not None:
            product_data.image_link = image_link
            isupload = handle_uploaded_file(image_link)
        product_data.description = description
        product_data.sku = sku
        product_data.sizes = sizes
        product_data.price = float(price)

        product_data.save()
        return HttpResponseRedirect('/products')
    return render(request, 'products/edit_product.html',
                  {'product': product_data})


@verify_request
@login_required
@user_passes_test(lambda user: user.is_superuser)
def delete_product(request, product_id):
    Product.objects.filter(id=int(product_id)).delete()
    return HttpResponseRedirect('/products')
