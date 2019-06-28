from django.shortcuts import render
from collector.models import Order, Bid

# Create your views here.


def order(request, number):
    order = Order.objects.get(number=number)
    if request.method == "POST":
        bid = Bid(order_id=order, name=request.POST['name'], phone=request.POST['phone'])
        bid.save()
        return render(request, 'collector/order_taken.html', {'order': order})
    else:
        return render(request, 'collector/order.html', {'order': order})


def error404(request, *args, **kwargs):
    return render(request, 'technical/404.html', status=404)


def error500(request, *args, **kwargs):
    return render(request, 'technical/500.html', status=500)


def in_development(request):
    return render(request, 'technical/in_development.html')
