from django.db import models


# Create your models here.
class CompanyModel(models.Model):
    company_name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.ImageField(blank=False, null=False, upload_to='CompanyLogo/')


class MottoHome(models.Model):
    title = models.CharField(max_length=1000, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    image = models.FileField(blank=False, upload_to='PartnerCompany/')
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class PartnerCompany(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    logo = models.FileField(blank=False, upload_to='PartnerCompany/')
    link = models.URLField(max_length=1000, blank=True, null=True)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    email = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.email


class CustomerService(CompanyModel):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    image = models.FileField(upload_to='CustomerService/', blank=False, null=False)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    image = models.FileField(upload_to='Feature/', blank=False, null=False)
    mirror_image = models.FileField(upload_to='Feature/', blank=True, null=True)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class AdvanceFeature(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    image = models.FileField(upload_to='AdvanceFeature/', blank=False, null=False)
    mirror_image = models.FileField(upload_to='AdvanceFeature/', blank=True, null=True)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class WorkingProcess(models.Model):
    step = models.CharField(max_length=10, blank=False, null=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    image = models.FileField(upload_to='WorkingProcess/', blank=False, null=False)
    mirror_image = models.FileField(upload_to='WorkingProcess/', blank=True, null=True)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.step + ' ' + self.title


class TestimonialHeader(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    designation = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=False, null=False)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' ' + self.title


class IntegratedCompany(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    image = models.FileField(upload_to='IntegratedCompany/', blank=False, null=False)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.name
