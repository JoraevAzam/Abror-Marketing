from uuid import uuid4
from django.conf import settings
from django.db import models
from django.urls import reverse


class CategoriesModels(models.Model):
    title1 = models.CharField(max_length=55)
    title2 = models.CharField(max_length=55)
    title3 = models.CharField(max_length=55)
    title4 = models.CharField(max_length=55)

    def __str__(self):
        return str(self.title1)


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = "images/{filename}".format(
        filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class BusinessSmmModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


class MainLogoModel(models.Model):
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.pk)


class TargetingModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


class LogoRoleModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)


class OurProjectsModel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body1 = models.TextField(blank=True, null=True)
    body2 = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_location, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image1.url)
        except:
            url = ''
        return url

    @property
    def imageURL2(self):
        try:
            url = str(self.image2.url)
        except:
            url = ''
        return url


    def __str__(self):
        return str(self.title)


class ContactModel(models.Model):
    nickname = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.nickname)


class CarouselModel(models.Model):
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.pk)


class ServicesModel(models.Model):
    service1 = models.CharField(max_length=55)
    service2 = models.CharField(max_length=55)
    service3 = models.CharField(max_length=55)
    service4 = models.CharField(max_length=55)
    service5 = models.CharField(max_length=55)
    service6 = models.CharField(max_length=55)
    service7 = models.CharField(max_length=55)

    def __str__(self):
        return str(self.pk)








