from django.db import models


# Create your models here.

class ServiceModel(models.CharField):
    name = models.CharField(max_length=200, blank=False)
    short_description = models.TextField(1000, blank=False, null=False)

    def __str__(self):
        return self.name


class ServiceDetailsModel(models.Model):
    pass


class PackageTypeModel(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class PriceModel(models.Model):
    validity_type = [
        ('day', 'day'),
        ('month', 'month'),
        ('year', 'year'),
    ]
    package = models.ForeignKey(PackageTypeModel, on_delete=models.CASCADE)
    price = models.CharField(max_length=100, blank=False, null=False)
    validity = models.CharField(choices=validity_type,max_length=100, blank=False, null=False)
    contains = models.TextField(max_length=2000, blank=False, null=False)

    def __str__(self):
        return self.package.name + ' price: ' + self.price
