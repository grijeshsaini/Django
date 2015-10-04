from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Status(models.Model):
    status_id = models.IntegerField(primary_key=True)
    status_name = models.CharField(max_length=200)


class CategoryMst(models.Model):
    # username = models.ForeignKey(User, 'username')
    category_id = models.BigIntegerField('category_id', unique=True)
    category_name = models.CharField(max_length=200)
    parent_id = models.BigIntegerField('parent_id', default=0)


class DisabledCategories(models.Model):
    username = models.ForeignKey(User, 'username')
    category = models.ForeignKey(CategoryMst, 'category_id')
    # status_id = models.ForeignKey(Status, 'status_id', default=2)  # Disabled


class Item(models.Model):
    username = models.ForeignKey(User, 'username')
    sub_category = models.ForeignKey(CategoryMst, 'category_id')
    item_id = models.BigIntegerField(unique=True)
    item_name = models.CharField(max_length=200)
    brand_id = models.IntegerField('brand_id', default=0)
    price = models.DecimalField('price', max_digits=20, decimal_places=5, default=0)
    qty = models.IntegerField('qty', default=1)


class TransactionDetails(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_date = models.DateTimeField('transaction_date')
    transaction_amount = models.DecimalField('transaction_amount', max_digits=20, decimal_places=5, default=0)
    username = models.ForeignKey(User, 'username', default='NULL')


class Order(models.Model):
    transaction = models.ForeignKey(TransactionDetails, 'transaction_id')
    item = models.ForeignKey(Item, 'item_id')
    qty = models.IntegerField('qty', default=1)
    price = models.DecimalField('price', max_digits=20, decimal_places=5, default=0)


class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=200)
