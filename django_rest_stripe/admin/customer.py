from django.contrib import admin
from django_rest_stripe.models import StripeCustomer
from django.conf import settings
import stripe


@admin.register(StripeCustomer)
class StripeCustomerAdmin(admin.ModelAdmin):
    readonly_fields = ['customer_id']

    def get_queryset(self, request):
        stripe.api_key = settings.STRIPE_API_KEY
        customer = stripe.Customer.list()
        print(customer)
        # for prod in products['data']:
        #     StripeProduct.objects.get_or_create(
        #         name=prod['name'],
        #         product_id=prod['id']
        #     )
        qs = super(StripeCustomerAdmin, self).get_queryset(request)
        return qs

    def save_model(self, request, obj, form, change):
        print(obj, form, change)
        # if not change:
        #     stripe.api_key = settings.STRIPE_API_KEY
        #     product = stripe.Customer.create(
        #         name=obj.name,
        #         type='service'
        #     )
        #     print(product)
        #     obj.product_id = product['id']
        #     obj.save()
