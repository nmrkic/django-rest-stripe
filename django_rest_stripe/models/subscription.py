from django.db import models
from django_rest_stripe.models.customer import StripeCustomer
from django_rest_stripe.models.products import StripePlan


class StripeSubscription(models.Model):
    customer = models.ForeignKey(StripeCustomer, null=False, on_delete=models.CASCADE)
    items = models.ManyToManyField(StripePlan, related_name="items")
    subscription_id = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
