import stripe
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status
from django_rest_stripe import models as m_django_rest_stripe
from django_rest_stripe import serializers as s_django_rest_stripe


class StripePlansAPI(APIView):

    def get(self, request):
        stripe.api_key = settings.STRIPE_API_KEY
        plans = m_django_rest_stripe.StripePlan.objects.filter(active=True)
        serializer = s_django_rest_stripe.StripePlanSerializer(plans, many=True)
        return Response({"plans": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        subs_data = request.data
        print("received token {}".format(request.data))
        stripe.api_key = settings.STRIPE_API_KEY
        customer = m_django_rest_stripe.StripeCustomer.objects.filter(email=subs_data['email']).first()
        if not customer:
            str_customer = stripe.Customer.create(
                    description="Customer for {}".format(subs_data['client']),
                    source=subs_data['token'],
                    name=subs_data['client'],
                    email=subs_data['email']
            )

            customer = m_django_rest_stripe.StripeCustomer.objects.create(
                customer_id=str_customer['id'],
                name=str_customer['name'],
                email=str_customer['email'],
                description=str_customer['description']
            )

        subscription = m_django_rest_stripe.StripeSubscription.objects.filter(customer_id=customer.id).first()
        if subscription:
            existing_subscription = stripe.Subscription.retrieve(subscription.subscription_id)
            new_plan = m_django_rest_stripe.StripePlan.objects.filter(plan_id=subs_data['plan']).first()
            items = [{'plan': subs_data['plan'], 'id': existing_subscription['items']['data'][0]['id']}]
            str_subscription = stripe.Subscription.modify(
                subscription.subscription_id,
                cancel_at_period_end=False,
                items=items
            )
            old_plan = subscription.items.first()
            subscription.items.remove(old_plan)
            subscription.items.add(new_plan)
            subscription.save()
        else:
            items = [{'plan': subs_data['plan']}]
            str_subscription = stripe.Subscription.create(
                    customer=customer.customer_id,
                    items=items,
                    collection_method="charge_automatically"
            )

            subscription, created = m_django_rest_stripe.StripeSubscription.objects.get_or_create(
                   subscription_id=str_subscription['id'],
                   customer_id=customer.id
                )

            if created:
                plan = m_django_rest_stripe.StripePlan.objects.get(plan_id=subs_data['plan'])
                subscription.items.add(plan)
                subscription.save()

        return Response(str_subscription, status=status.HTTP_200_OK)

    def delete(self, request):
        subs_data = request.data
        stripe.api_key = settings.STRIPE_API_KEY
        customer = m_django_rest_stripe.StripeCustomer.objects.filter(email=subs_data['email']).first()
        if not customer:
            str_customer = stripe.Customer.create(
                    description="Customer for {}".format(subs_data['client']),
                    source=subs_data['token'],
                    name=subs_data['client'],
                    email=subs_data['email']
            )

            customer = m_django_rest_stripe.StripeCustomer.objects.create(
                customer_id=str_customer['id'],
                name=str_customer['name'],
                email=str_customer['email'],
                description=str_customer['description']
            )

        subscription = m_django_rest_stripe.StripeSubscription.objects.filter(customer_id=customer.id).first()
        if subscription:
            stripe.Subscription.delete(subscription.subscription_id)
            subscription.delete()

        return Response({}, status=status.HTTP_200_OK)
