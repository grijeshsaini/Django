from collections import namedtuple
from django.contrib.auth.models import User
from django.db import connection
from market.models import DisabledCategories, CategoryMst
from market.queries import ALL_ITEM_QUERY

__author__ = 'grijesh'

# This File contains generic functions which can be used across the multiple views (controllers)
# Following DRY principle


def getallitems():
    # This will close the connection
    with connection.cursor() as c:
        c.execute(ALL_ITEM_QUERY)
        return namedtuplefetchall(c)


def getuseritems(userid):
    # This will close the connection
    with connection.cursor() as c:
        # we must pass parameter as a prepared statement
        # todo refractor parameter passing way (Done)
        # c.execute(ALL_ITEM_QUERY + " and au.username = '"+userid+"'")
        c.execute(ALL_ITEM_QUERY + " and au.username = %s", userid)
        return namedtuplefetchall(c)


def namedtuplefetchall(cursor):
    """Return all rows from a cursor as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def disablecategory(username, categoryid):
    row = DisabledCategories(username=User.objects.get_by_natural_key(username),
                             category=CategoryMst.objects.get(category_id=categoryid))
    row.save()


def enablecategory(username, categoryid):
    DisabledCategories.objects.filter(username=username, category=categoryid).delete()


# def addItem()