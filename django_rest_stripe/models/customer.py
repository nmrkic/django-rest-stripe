from django.db import models


class StripeCustomer(models.Model):
    email = models.EmailField()
    source = models.CharField(max_length=150)
    customer_id = models.CharField(max_length=150)
