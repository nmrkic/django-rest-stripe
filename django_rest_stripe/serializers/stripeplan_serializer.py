from rest_framework import serializers
from django_rest_stripe import models as m_django_rest_stripe


class StripePlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = m_django_rest_stripe.StripePlan
        exclude = ['id', 'product', 'active']
