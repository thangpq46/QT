# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    id = models.OneToOneField('self', models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.CharField(max_length=45)
    parent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Order(models.Model):
    orderid = models.IntegerField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='Total')  # Field name made lowercase.
    status = models.IntegerField(db_column='Status')  # Field name made lowercase.
    dateplaceorder = models.DateTimeField(db_column='DatePlaceOrder')  # Field name made lowercase.
    datecomplete = models.DateTimeField(db_column='DateComplete')  # Field name made lowercase.
    orderaddress = models.CharField(db_column='OrderAddress', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Orderdetails(models.Model):
    detailsid = models.IntegerField(db_column='DetailsID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    order = models.ForeignKey(Order, models.DO_NOTHING, db_column='Order')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetails'


class Pricing(models.Model):
    idpricing = models.IntegerField(db_column='idPricing', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    date_created = models.DateTimeField()
    date_expiry = models.DateTimeField()
    in_active = models.IntegerField()
    baseprice = models.CharField(db_column='BasePrice', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pricing'


class Product(models.Model):
    idproduct = models.IntegerField(db_column='idProduct', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=225)  # Field name made lowercase.
    image = models.CharField(db_column='Image', max_length=255)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock', blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(Category, models.DO_NOTHING, db_column='Category')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'
        unique_together = (('idproduct', 'image'),)


class ProductDiscount(models.Model):
    id = models.IntegerField(primary_key=True)
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    discountvalue = models.FloatField(db_column='DiscountValue')  # Field name made lowercase.
    discountunit = models.CharField(db_column='DiscountUnit', max_length=20)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    from_field = models.DateTimeField(db_column='From')  # Field name made lowercase. Field renamed because it was a Python reserved word.
    until = models.DateTimeField(db_column='Until')  # Field name made lowercase.
    couponcode = models.CharField(db_column='CouponCode', max_length=10)  # Field name made lowercase.
    minimumordervalue = models.FloatField(db_column='MinimumOrderValue')  # Field name made lowercase.
    is_redeem_allowed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_discount'
