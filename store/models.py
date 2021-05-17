from django.db import models
from django.contrib.auth.models import User
from  django.urls import reverse
from  django.conf import settings


class ShoeManager(models.Manager):
    def get_queryset(self):
        return  super(ShoeManager, self).get_queryset().filter(is_active=True)


class Brand(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/brand')

    class Meta:
        verbose_name_plural = 'Brands'

    def __str__(self):
        return  self.name

    def get_absolute_url(self):
        return  reverse('store:brand_shoe', args=[self.slug])


class Shoe(models.Model):
    brand_id = models.ForeignKey(Brand,related_name='brand_shoe', on_delete=models.CASCADE)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='shoes_creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/shoes')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created = models.TimeField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Shoes'
        ordering = ('-updated',)

    def __str__(self):
        return  self.title

    def get_absolute_url(self):
        return  reverse('store:shoe_detail', args=[self.slug])