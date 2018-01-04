from django.shortcuts import render
from mokebe_main import models as shop_models


def index(request):
    shop_items = shop_models.ShopItem.objects.all()
    return render(request,
                  'index.html',
                  {
                      'shop_items': shop_items,
                  })
