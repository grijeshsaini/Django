import os
import django

# These lines are required at this place to solve below error
# django.core.exceptions.ImproperlyConfigured:
# Requested setting CACHES, but settings are not configured.
# You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure()
#  before accessing settings.

os.environ['DJANGO_SETTINGS_MODULE'] = 'marketplace.settings'
django.setup()


# To import unittest please install nose (pip install nose)
from unittest import TestCase
from django.core.urlresolvers import resolve
from market.marketdao import getallitems,getuseritems
import logging
from market.service import disableUserCategory, enableUserCategory, getitems

logger = logging.getLogger()


class MarketPlaceViewTest(TestCase):

    def setUp(self):
        # Importing Project Specific Settings
        # Init
        os.environ['DJANGO_SETTINGS_MODULE'] = 'marketplace.settings'
        django.setup()

    def test_login(self):
        # SUT (Service Under Test)
        resolver = resolve('/accounts/')
        # Assert
        self.assertEqual(resolver.view_name, 'market.views.login')

    def test_logged_in(self):
        # SUT
        resolver = resolve('/accounts/loggedin/')
        # Assert
        self.assertEqual(resolver.view_name, 'market.views.loggedin')

    def test_order_view_get_all_item(self):
        # This test is just written to test the select query
        # It should be disabled or we should use mock data
        logger.info(getitems()[0])
        self.assertIsNotNone(getitems()[0])

    def test_order_view_get_user_item(self):
        # This test is just written to test the select query
        # It should be disabled or we should use mock data
        logger.info(getuseritems('grijesh1'))
        self.assertIsNotNone(getuseritems('grijesh1')[0])

    def test_disable_user_category(self):
        disableUserCategory('grijesh1',1)
        pass

    def test_enable_user_category(self):
        enableUserCategory('grijesh1',1)
        pass