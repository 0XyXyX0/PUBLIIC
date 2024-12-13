
from django.core.management.base import BaseCommand
from shop.models import Tag, Item, Category
from django.db.models import (
    Sum,
    Avg,
    Count,
    Min,
    Max,
    Q,
    F,
)

class Command(BaseCommand):
    def handle(self, *args, **options):
        
        items = Category.objects.aggregate(count_items=Count('items'))
        # print(items)

        items_price = Item.objects.aggregate(
            min_price=Min('price'),
            max_price=Max('price'),
            avg_price=Avg('price')
        )
        # print(items1)

        items1 = Category.objects.annotate(item_count=Count('items'))
        # for item in items1:
        #     print(item.name, item.item_count)

        items_sum_price = Category.objects.annotate(sum_price=Sum('items__price', default=0))
        # for item in items_sum_price:
        #     print(item.sum_price)


        items2 = Item.objects.select_related().all()
        # for item in items2:
        #     print(item)

        items3 = Category.objects.select_related().all()
        # for item in items3:
        #     print(item)

        item_tags = Tag.objects.prefetch_related('items').all()
        # for item in item_tags:
        #     print(item.name)