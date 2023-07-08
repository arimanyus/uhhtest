from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Template(models.Model):
    name = models.CharField(max_length=255)
    template_file = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Site(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    template_name = models.CharField(max_length=255, default='walnut')
    color_scheme = models.CharField(max_length=200, default='light')
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    industry = models.CharField(max_length=200, default='Other')
    description = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserWebsite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    template_name = models.CharField(max_length=200)
    color_scheme = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    industry = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.user.username


class Website(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    template_name = models.CharField(max_length=100)
    description = models.TextField()
    industry = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    color_scheme = models.CharField(max_length=100)
