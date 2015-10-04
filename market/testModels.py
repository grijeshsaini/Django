import os
import django
from nose.plugins import skip

os.environ['DJANGO_SETTINGS_MODULE'] = 'marketplace.settings'
django.setup()

from django.test import TransactionTestCase
from django.db import transaction
from market.models import User

__author__ = 'grijesh'


class TestMarketPlaceModel(TransactionTestCase):
    cleans_up_after_itself = True

    def testUserInsert(self):
        # Initialization
        User.objects.create_user('test2', 'test@xyz.com', 'test123')
        self.assertEqual('test1', 'test1')

    @classmethod
    def tearDown(self):
        transaction.rollback(User)
