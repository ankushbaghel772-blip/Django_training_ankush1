from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import product
from django.urls import reverse


# Create Product Form
def newProductForm(request):
    res = render(request, 'newProductForm.html')
    return res


# CREATE PRODUCT
def saveproduct(request):
    pid = request.POST['pid']
    pname = request.POST['pname']
    pprice = request.POST['pprice']
    poffer = request.POST['poffer']

    prod = product(
        pid=pid,
        pname=pname,
        pprice=pprice,
        poffer=poffer
    )

    prod.save()

    url = reverse('productlist')
    return HttpResponseRedirect(url)


# READ PRODUCTS
def productlist(request):
    Products = product.objects.all()

    res = render(
        request,
        'productlist.html',
        {'Products': Products}
    )

    return res


# UPDATE PRODUCT FORM
def updateproductform(request):
    id = request.GET['id']

    Product = product.objects.filter(id=id).values()

    res = render(
        request,
        'updateproductform.html',
        {'Product': Product[0]}
    )

    return res


# UPDATE PRODUCT
def updateproduct(request):
    id = request.POST['id']
    pid = request.POST['pid']
    pname = request.POST['pname']
    pprice = request.POST['pprice']
    poffer = request.POST['poffer']

    product(
        id=id,
        pid=pid,
        pname=pname,
        pprice=pprice,
        poffer=poffer
    ).save()

    url = reverse('productlist')
    return HttpResponseRedirect(url)


# DELETE PRODUCT
def deleteproduct(request):
    id = request.GET['id']

    prod = product.objects.filter(id=id)
    prod.delete()

    url = reverse('productlist')
    return HttpResponseRedirect(url)