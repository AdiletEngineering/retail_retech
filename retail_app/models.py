from django.db import models


class Product(models.Model):
    name = models.CharField("Name of product", max_length=200)
    barcode = models.CharField("Product barcode", max_length=8)

    def __str__(self):
        return self.name


class Store(models.Model):
    branch_name = models.CharField("Name of store branch", max_length=200)
    location = models.CharField("location of store", max_length=200)

    def __str__(self):
        return self.branch_name


class Supply(models.Model):
    products = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='supplies')
    stores = models.ForeignKey(Store, on_delete=models.DO_NOTHING, related_name='supplies')
    supply_date = models.DateTimeField(auto_now_add=True)
    quantity = models.FloatField("supply product quantity")

    def __str__(self):
        return self.id


class Sale(models.Model):
    products = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='sales')
    stores = models.ForeignKey(Store, on_delete=models.DO_NOTHING, related_name='sales')
    sale_date = models.DateTimeField(auto_now_add=True)
    quantity = models.FloatField("sale product quantity")

    def __str__(self):
        return self.id
