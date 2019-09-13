from django.contrib import admin
from django_rest_stripe.models import StripeSubscription, StripePlan, StripeCustomer
from django.conf import settings
import stripe


@admin.register(StripeSubscription)
class StripeSubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ['subscription_id']
    list_display = ['customer', 'subscription_id', 'list_plans']
    actions = ['unsubscribe']

    def list_plans(self, obj):
        plans = [str(x) for x in obj.items.all()]
        return ','.join(plans)

    def get_queryset(self, request):
        stripe.api_key = settings.STRIPE_API_KEY
        subscriptions = stripe.Subscription.list()
        print(subscriptions)
        plans = []
        for prod in subscriptions['data']:
            for item in prod['items']['data']:
                plans.append(StripePlan.objects.get(plan_id=item['plan']['id']))
            customer = StripeCustomer.objects.get(customer_id=prod['customer'])
            subscription, created = StripeSubscription.objects.get_or_create(
               subscription_id=prod['id'],
               customer_id=customer.id
            )
            if created:
                subscription.items.add(*plans)
                subscription.save()
        qs = super(StripeSubscriptionAdmin, self).get_queryset(request)
        return qs

    def save_model(self, request, obj, form, change):
        print(obj, form, change)
        if not change:
            print(form.clean())
            form.save()
            stripe.api_key = settings.STRIPE_API_KEY
            items = [{"plan": x.plan_id} for x in obj.items.all()]
            print(items, obj.items.all())
            subscription = stripe.Subscription.create(
                customer=obj.customer.customer_id,
                items=items,
                collection_method="charge_automatically"
            )
            print(subscription)
            obj.subscription_id = subscription['id']
            obj.save()

    def unsubscribe(modeladmin, request, queryset):
        for obj in queryset:
            stripe.Subscription.delete(obj.subscription_id)
            obj.delete()
