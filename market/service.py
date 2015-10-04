
from market.marketdao import getuseritems, getallitems, disablecategory, enablecategory
import logging

__author__ = 'grijesh'
logger = logging.getLogger()
# This class is going to contain the business logic over DAO objects


def getitems():
    try:
        return getallitems()
    except Exception as e:
        logger.error(e.message)
        raise


def getmyitems(userid):
    try:
        return getuseritems(userid)
    except Exception as e:
        logger.error(e.message)
        raise


def disableUserCategory(username, categoryid):
    try:
        disablecategory(username, categoryid)
    except Exception as e:
        logger.error(e.message)
        raise


def enableUserCategory(username, categoryid):
    try:
        enablecategory(username, categoryid)
    except Exception as e:
        logger.error(e.message)
        raise

