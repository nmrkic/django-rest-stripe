#This file mainly exists to allow python setup.py test to work.
import os
import sys
from django.test.utils import get_runner
from django.conf import settings

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_rest_stripe.settings.test'
test_dir = os.path.join(os.path.dirname(__file__), "djanog_rest_stripe")
sys.path.insert(0, test_dir)


def runtests():
    test_runner = get_runner(settings)
    failures = test_runner([], verbosity=1, interactive=True).run_tests(['django_rest_stripe'])
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
