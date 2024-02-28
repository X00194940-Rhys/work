from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def prod_list(request):

    products = Product.objects.filter(available=True)

    paginator = Paginator(products, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)
        
    return render(request, 'shop/product_list.html', {'prods': products})


def product_detail(request, product_id):
    # Assuming you've removed references to categories
    # and accessing products directly by their ID

    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})
