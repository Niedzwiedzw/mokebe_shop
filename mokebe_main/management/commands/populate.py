from django.core.management.base import BaseCommand, CommandError
from mokebe_main.models import ShopItem


class Command(BaseCommand):
    help = 'populates database with items'

    def handle(self, *args, **options):
        for i in range(200):
            ShopItem.objects.create(
                producer_code=f'kod_producenta_{i}',
                name=f'jakas_czesc_{i}',
                price_net=100 + i + i*2/100,
                vat_value=((i % 3) + 20)/100,
                quantity=i,
            ).save()
        print(f"dodano {i+1} obiektow")
