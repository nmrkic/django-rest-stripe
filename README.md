# Django Stripe

Django Stripe is a simple Django package which provides models, APIs and Django admin pages for setting up products and receiving payments over Stripe.

1. Add django_rest_stripe to INSTALLED_APPS:
```
INSTALLED_APPS = [
    .....
    'django_rest_stripe'
]
```
2. Include django_rest_stripe URLconf in urls.py:
```
url(r'^api/stripe', include('django_rest_stripe.urls'))
```
3. Run `python manage.py migrate`

4. Run the development server and access http://127.0.0.1:8000/admin/ to manage Stripe products and payments
