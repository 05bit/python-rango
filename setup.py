# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup

version = '0.0.2a'

LONG_DESCRIPTION = """
Rango is a new taste of Django. In general it provides shorter
API calls for Django and some extra helpers.
"""

def long_description():
    """Return long description from README.md if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(
    name='rango',
    version=version,
    author='Alexey Kinyov',
    author_email='rudy@05bit.com',
    description='Rango is a spicey API to Django with some extras.',
    license='MIT',
    keywords='django, utils, sugar',
    url='https://github.com/05bit/rango',
    packages=['rango', 'rango.db', 'rango.auth'],
    long_description=long_description(),
    install_requires=['Django>=1.4', 'unidecode'],
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Operating System :: OS Independent',
                 'License :: OSI Approved :: BSD License',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7'])
