from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    product = Product.objects.get(id=request.POST['product_id'])
    quantity_from_form = int(request.POST["quantity"])
    total_charge = quantity_from_form * product.price
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/success')

def success(request):
    thisOrder = Order.objects.last()
    orders = Order.objects.all()
    totalItems = 0
    totalMoney = 0
    for order in orders:
        totalItems += order.quantity_ordered
        totalMoney += order.total_price
    context = {
        'totalCharge': thisOrder.total_price,
        'totalItems': totalItems,
        'totalMoney': totalMoney,
    }
    return render(request, "store/checkout.html", context)