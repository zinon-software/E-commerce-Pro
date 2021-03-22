from django.shortcuts import render, redirect

from .forms import *

# Create your views here.

def dashboard(request):
    shippingOrder = ShippingAddress.objects.order_by('-id')
    Items = OrderItem.objects.all()
    the_sales = sum([item.get_total for item in Items])

    context = {
        'shippingOrder': shippingOrder,
        'cartItems': shippingOrder.count(),
        'customer': Customer.objects.all().count(),
        'Items': Items,
        'the_sales': the_sales,

    }

    return render(request, 'dashboard/index.html', context)


def tables(request, order):
    orders = OrderItem.objects.all()
    filterOrder = orders.filter(order=order)

    address = ShippingAddress.objects.all()
    filterAddress = address.filter(order=order)

    total = sum([item.get_total for item in filterOrder])

    Items = sum([item.quantity for item in filterOrder])

    context = {
        'filterOrder': filterOrder,
        'filterAddress': filterAddress,
        'total': total,
        'Items': Items,
    }

    return render(request, 'dashboard/tables.html', context)

def charts(request):

    return render(request, 'dashboard/charts.html')


def forms(request):
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            product_item = form.save(commit=False)
            product_item.save()

            return redirect('/forms/')
    else:
        form = ProductForms()

    context = {
        'form': form,
    }

    return render(request, 'dashboard/forms.html', context)