# -*- coding: utf-8 -*-

from django.shortcuts import render
from collector.models import Order, Bid
import requests
import json
import datetime

# Create your views here.


def order(request, number):
    order = Order.objects.get(number=number)
    if request.method == "POST":
        bid = Bid(order_id=order, name=request.POST['name'], phone=request.POST['phone'], comment=request.POST['comment'])
        bid.save()
        write_event('order_taken', order.number)
        return render(request, 'collector/order_taken.html', {'order': order})
    else:
        write_event('order_open', order.number)
        return render(request, 'collector/order.html', {'order': order})


def error404(request, *args, **kwargs):
    return render(request, 'technical/404.html', status=404)


def error500(request, *args, **kwargs):
    return render(request, 'technical/500.html', status=500)


def in_development(request):
    return render(request, 'technical/in_development.html')


def write_event(event, order_id):

    url = 'https://metrika.trucker.group/events'
    headers = {'content-type': 'application/json;charset=UTF-8'}
    data_raw = '{"events": [' \
               '{' \
               '"user_id": -1,' \
               '"tags": ["bidok"],' \
               '"name": "'+event+'",' \
               '"happened_at": "'+str(datetime.datetime.now())+'",' \
               '"data": {"order": '+order_id+'}' \
               '}' \
               ']}'

    data = json.loads(data_raw)
    response = requests.post(url, data=json.dumps(data), headers=headers)

