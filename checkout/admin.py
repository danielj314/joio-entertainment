from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date',
                       'order_total', 'deposit_payed',
                       'remaining_balance', 'original_bag',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'event_date',
              'event_time', 'event_location', 'event_postcode',
              'full_name', 'email', 'phone_number',
              'street_address1', 'street_address2',
              'town_or_city', 'postcode',
              'order_date', 'order_total',
              'deposit_payed', 'remaining_balance',
              'original_bag', 'stripe_pid')

    list_display = ('order_number', 'order_date', 'full_name',
                    'event_location', 'event_date', 'order_total', 
                    'deposit_payed', 'remaining_balance',)

    ordering = ('event_date',)


admin.site.register(Order, OrderAdmin)
