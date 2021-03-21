from django.shortcuts import render, redirect

from .forms import *

# Create your views here.

def dashboard(request):

    return render(request, 'dashboard/index.html')


def tables(request):

    return render(request, 'dashboard/tables.html')

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