from django.db import models
from django_rest_stripe.models.customer import StripeCustomer
from django_rest_stripe.models.products import StripeProduct


class StripSubscription(models.Model):
    customer = models.ForeignKey(StripeCustomer, null=False)
    items = models.ManyToManyField(StripeProduct)
    subscription_id = models.CharField()
