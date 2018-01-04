from django.db import models
from decimal import *


class ShopItem(models.Model):
    producer_code = models.CharField(max_length=128, verbose_name='Kod producenta')
    name = models.CharField(max_length=256, verbose_name='Nazwa')
    price_net = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Cena netto')
    quantity = models.IntegerField(verbose_name='Stan')
    vat_value = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='Stawka VAT')

    @property
    def price_plus_vat(self):
        return (self.price_net * ((self.vat_value / 100) + 1)).quantize(Decimal("0.00"))
