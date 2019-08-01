from django.contrib import admin
from django_rest_stripe.models import StripeProduct, StripePlan
from django.conf import settings
import stripe


@admin.register(StripeProduct)
class StripeProductAdmin(admin.ModelAdmin):
    readonly_fields = ['product_id']

    def get_queryset(self, request):
        stripe.api_key = settings.STRIPE_API_KEY
        products = stripe.Product.list()
        print(products)
        for prod in products['data']:
            StripeProduct.objects.get_or_create(
                name=prod['name'],
                product_id=prod['id']
            )
        qs = super(StripeProductAdmin, self).get_queryset(request)
        return qs

    def save_model(self, request, obj, form, change):
        print(obj, form, change)
        if not change:
            stripe.api_key = settings.STRIPE_API_KEY
            product = stripe.Product.create(
                name=obj.name,
                type='service'
            )
            print(product)
            obj.product_id = product['id']
            obj.save()


@admin.register(StripePlan)
class StripePlanAdmin(admin.ModelAdmin):
    readonly_fields = ['plan_id']

    def get_queryset(self, request):
        stripe.api_key = settings.STRIPE_API_KEY
        plans = stripe.Plan.list()
        print(plans)
        # for prod in plans['data']:
        #     StripePlan.objects.get_or_create(
        #         name=prod['name'],
        #         product_id=prod['id']
        #     )
        qs = super(StripePlanAdmin, self).get_queryset(request)
        return qs

    def save_model(self, request, obj, form, change):
        print(obj, form, change)
        if not change:
            stripe.api_key = settings.STRIPE_API_KEY
            plan = stripe.Plan.create(
                product=obj.product.product_id,
                nickname=obj.nickname,
                interval=obj.interval,
                currency=obj.currency,
                amount=obj.amount,
            )
            print(plan)
            obj.plan_id = plan['id']
            obj.save()

