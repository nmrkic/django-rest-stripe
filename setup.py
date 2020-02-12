import os
import re
import codecs
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    """
    Reads out software version from provided path(s).
    """
    version_file = read(*file_paths)
    lookup = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                       version_file, re.M)

    if lookup:
        return lookup.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name='django-rest-stripe',
    version=find_version('django_rest_stripe', '__init__.py'),
    packages=['django_rest_stripe'],
    include_package_data=True,
    license='Apache 2.0',
    description='Django Rest Stripe payment implementation.',
    long_description=README,
    author='Nebojsa Mrkic',
    author_email='mrkic.nebojsa@gmail.com',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ],
    install_requires=[
        "Django==2.2.10",
        "djangorestframework==3.10.1",
        "stripe==2.32.1"
    ]
)

