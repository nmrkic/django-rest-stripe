import stripe
from django_rest_stripe import models as m_djanog_rest_stripe
from django.conf import settings


def check_subscription(client):
    stripe.api_key = settings.STRIPE_API_KEY
    customer = m_djanog_rest_stripe.StripeCustomer.objects.filter(name=client).first()
    if customer:
        subscription = m_djanog_rest_stripe.StripeSubscription.objects.filter(customer=customer).first()
        if subscription:
            str_subscription = stripe.Subscription.retrieve(subscription.subscription_id)
            print(str_subscription)
            if str_subscription['status'] == 'active':
                return {
                    'plan_id': str_subscription.plan.id
                }
    return None
