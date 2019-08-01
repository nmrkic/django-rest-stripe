from .dev import *  # noqa

DEBUG = True


TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-erase',
    '--cover-package=django_rest_stripe'
]

ROOT_URLCONF = 'django_rest_stripe.django_rest_stripe.urls'
