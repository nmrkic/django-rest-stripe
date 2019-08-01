import stripe
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


class StripeProductAPI(APIView):

    def get(self, request):
        stripe.api_key = settings.STRIPE_API_KEY
        return Response({}, status=status.HTTP_200_OK)

    def put(self, request):
        stripe.api_key = settings.STRIPE_API_KEY
        return Response({}, status=status.HTTP_200_OK)

    def post(self, request):
        stripe.api_key = settings.STRIPE_API_KEY
        return Response({}, status=status.HTTP_200_OK)
