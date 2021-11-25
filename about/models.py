from django.db import models


# Create your models here.
class MottoAbout(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    image1 = models.FileField(upload_to='AboutImage/', blank=False, null=False)
    image2 = models.FileField(upload_to='AboutImage/', blank=False, null=False)
    image3 = models.FileField(upload_to='AboutImage/', blank=False, null=False)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TeamHeader(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    designation = models.CharField(max_length=300, blank=False, null=False)
    image = models.FileField(upload_to='TeamMember/', blank=True)
    linkedin = models.URLField(max_length=1000, blank=True, null=True)
    twitter = models.URLField(max_length=1000, blank=True, null=True)
    git = models.URLField(max_length=1000, blank=True, null=True)
    fb = models.URLField(max_length=1000, blank=True, null=True)
    visibility = models.BooleanField(default=False)


class OurStory(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.CharField(max_length=1000, blank=False, null=False)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OurAward(models.Model):
    name = models.CharField(max_length=300, blank=False, null=False)
    image = models.FileField(upload_to='OurAward/')
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class FAQModel(models.Model):
    question = models.CharField(max_length=500, blank=False, null=False)
    answer = models.CharField(max_length=1000, blank=False, null=False)
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.question
