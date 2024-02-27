from django.db import models

# Create your models here.

class Customer(models.Model):
    name =models.CharField(max_length=190,null=True)
    email =models.CharField(max_length=190,null=True)
    phone =models.CharField(max_length=190,null=True)
    age =models.CharField(max_length=190,null=True)
    date_created =models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=190, null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    CAT= (
        ('Classics','Classics'),
        ('Commic Book','Comic Book'),
        ('Fantasy','Fantasy'),
        ('Horror','Horror'),
        ('Programming','Programming'),
    )
    name =models.CharField(max_length=190,null=True)
    author =models.CharField(max_length=190,null=True)
    price =models.FloatField(null=True)
    fk_tag=models.ManyToManyField(Tag)
    category =models.CharField(max_length=200,null=True,choices=CAT)
    description =models.CharField(max_length=190,null=True)
    date_created =models.DateTimeField(max_length=190,null=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    STATUS= (
        ('Pending','Pending'),
        ('Delevered','Delevered'),
        ('in progress','in progress'),
        ('out of order','out of order'),
    )
    fk_customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    fk_book=models.ForeignKey(Book,null=True,on_delete=models.SET_NULL)
    fk_tag=models.ManyToManyField(Tag)
    date_created =models.DateTimeField(max_length=190,null=True)
    status =models.CharField(max_length=200,choices=STATUS,null=True)