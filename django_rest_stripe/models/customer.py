from django.db import models


class StripeCustomer(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=150, null=True, blank=True)
    source = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    customer_id = models.CharField(max_length=150)

    def __str__(self):
        return self.email
