from django.db import models
from datetime import datetime

def dateupdate():
    x=datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
    print(x)
    return x

class Category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45,unique=True)
    parent = models.ForeignKey('Category',blank=True, null=True,on_delete=models.CASCADE)

    class Meta:
        db_table = 'category'

    def __str__(self):
      return self.name

class Product(models.Model):
    productid = models.IntegerField(primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=225,unique=True)  # Field name made lowercase.
    image = models.ImageField( max_length=255)  # Field name made lowercase.
    stock = models.IntegerField( blank=True, null=True)  # Field name made lowercase.
    category = models.ForeignKey(Category, models.DO_NOTHING)  # Field name made lowercase.

    class Meta:
        db_table = 'product'
        unique_together = (('productid', 'image'),)

    def __str__(self):
      return self.name


class Order(models.Model):
    orderid = models.AutoField( primary_key=True)  # Field name made lowercase.
    total = models.IntegerField()  # Field name made lowercase.
    status = models.IntegerField(default=0)  # Field name made lowercase.
    dateplaceorder = models.DateTimeField(default=dateupdate())  # Field name made lowercase.
    datecomplete = models.DateTimeField(blank=True,null=True)  # Field name made lowercase.
    orderaddress = models.CharField( max_length=255)  # Field name made lowercase.

    class Meta:
        db_table = 'order'


class Orderdetails(models.Model):
    detailsid = models.IntegerField( primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, )  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    order = models.ForeignKey(Order, models.DO_NOTHING)  # Field name made lowercase.

    class Meta:
        db_table = 'orderdetails'


class Pricing(models.Model):
    pricingid = models.IntegerField( primary_key=True)  # Field name made lowercase.
    product = models.ForeignKey('Product', models.DO_NOTHING)  # Field name made lowercase.
    date_created = models.DateTimeField()
    date_expiry = models.DateTimeField()
    in_active = models.BooleanField()
    baseprice = models.CharField( max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'pricing'


class ProductDiscount(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)  # Field name made lowercase.
    discountvalue = models.FloatField()  # Field name made lowercase.
    discountunit = models.CharField( max_length=20)  # Field name made lowercase.
    createdate = models.DateTimeField()  # Field name made lowercase.
    from_field = models.DateTimeField()  # Field name made lowercase. Field renamed because it was a Python reserved word.
    until = models.DateTimeField()  # Field name made lowercase.
    couponcode = models.CharField( max_length=10)  # Field name made lowercase.
    minimumordervalue = models.FloatField()  # Field name made lowercase.
    is_redeem_allowed = models.IntegerField()

    class Meta:
        db_table = 'product_discount'
