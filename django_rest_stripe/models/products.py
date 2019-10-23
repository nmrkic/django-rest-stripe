from django.db import models

PLAN_INTERVAL = [
    ('day', 'day'),
    ('week', 'week'),
    ('month', 'month'),
    ('year', 'year'),
    ('quarterly', 'quarterly'),
]


class StripeProduct(models.Model):
    name = models.CharField(max_length=200)
    product_id = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class StripePlan(models.Model):
    plan_id = models.CharField(max_length=150)
    product = models.ForeignKey(StripeProduct, null=False, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=150)
    interval = models.CharField(max_length=10, choices=PLAN_INTERVAL)
    currency = models.CharField(max_length=150)
    amount = models.IntegerField()
    active = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nickname
