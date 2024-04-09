from django.db import models
from django.contrib.auth.models import User


# Create your models here.

CATEGORY_CHOICES=(
    ('Standard', 'Standard'),
    ('Premium', 'Premium'),
    ('Professional', 'Professional'),
)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    # city = models.CharField(max_length=200)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=100)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile.images/', blank=True, null=True)

    def __str__(self):
        return self.user.username


# class Order(models.Model):
#     STATUS = (
#         {'Pending', 'Pending'},
#         {'Out for payment', 'Out for payment'},
#         {'Paid', 'Paid'},
#     )
#     customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
#     product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     status = models.CharField(max_length=200, null=True, choices=STATUS)


# class Payment(models.Model):
#     STATUS = (
#         {'£500 - £5999', '£500 - £5999'},
#         {'£6000 - £29999', '£6000 - £29999'},
#         {'£30000 - £1000000', '£30000 - £1000000'}
#     )
#     customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
#     product = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)
#     status= models.CharField(max_length=200, null=True, choices=STATUS)
#     date_created = models.DateTimeField(auto_now_add=True, null=True)