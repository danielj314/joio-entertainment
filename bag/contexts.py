from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    if total < 1000:
        deposit = total / 2
    else:
        deposit = 500

    remaining_balance = total - deposit

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'deposit': deposit,
        'remaining_balance': remaining_balance,
    }

    return context
