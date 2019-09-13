from django.contrib import admin
from django_rest_stripe.models import StripeCustomer
from django.conf import settings
import stripe
import logging

logger = logging.getLogger(__name__)

@admin.register(StripeCustomer)
class StripeCustomerAdmin(admin.ModelAdmin):
    readonly_fields = ['customer_id']
    actions = ['delete_customers']

    def get_queryset(self, request):
        stripe.api_key = settings.STRIPE_API_KEY
        customers = stripe.Customer.list()
        print(customers)
        for prod in customers['data']:
            customer = StripeCustomer.objects.filter(customer_id=prod['id'], email=prod['email']).first()
            if customer:
                customer.source = prod['default_source'],
                customer.save()
            else:
                StripeCustomer.objects.create(
                    customer_id=prod['id'],
                    email=prod['email'],
                    description=prod['description'],
                    name=prod['name'],
                    source=prod['default_source']
                )
        qs = super(StripeCustomerAdmin, self).get_queryset(request)
        return qs

    def save_model(self, request, obj, form, change):
        print(obj, form, change)
        if not change:
            stripe.api_key = settings.STRIPE_API_KEY
            customer = stripe.Customer.create(
                description=obj.description,
                source=obj.source,
                email=obj.email,
                name=obj.name
            )
            print(customer)
            obj.customer_id = customer['id']
            obj.save()

    def delete_customers(modeladmin, request, queryset):
        for obj in queryset:
            try:
                stripe.Customer.delete(obj.customer_id)
            except Exception as e:
                logger.info("Customer error {}".format(str(e)))
            obj.delete()
