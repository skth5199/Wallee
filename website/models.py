from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class profile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,default=None,unique=True)
    name = models.TextField(default=None, null=True )
    address = models.TextField(default=None, null=True)
    dob = models.DateField( null=True)
    phone = models.CharField(max_length=15,default=None,blank=True, null=True)
    country = models.TextField(default=None, null=True)
    count=models.IntegerField(default=0)
    account=models.TextField(default='AF' , null=True)



class wallet(models.Model):
    amount = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=None, unique=True)





class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True ,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img =  models.ImageField()

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class item(models.Model):
    Name = models.TextField(primary_key=True)
    Cost = models.IntegerField()



class savedcards(models.Model):
    ownername = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name=models.TextField(default='aa' , null=True)
    number=models.TextField(default='aaa' , null=True)
    month=models.TextField(default='aa' , null=True)
    year=models.TextField(default='aa' , null=True)
    cvv=models.TextField(default='aa',null=True)

    amount = models.IntegerField(default=10000,null=True)
    password=models.CharField(default='2606',max_length=15,null=True)

class bankaccount(models.Model):
    username=models.TextField(default='' , null=True)
    number=models.TextField(default='' , null=True)
    ifsc=models.TextField(default='' , null=True)
    password=models.TextField(default='' , null=True)
    amount=models.IntegerField(default=10000)




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, unique=True)
    #item1 = models.ForeignKey(item, on_delete=models.CASCADE,default=None)
    i1c = models.TextField(default=False)
    q1c = models.IntegerField(default=1)
    #item2 = models.ForeignKey(item, on_delete=models.CASCADE,default=None)
    i2c = models.TextField(default=False)
    q2c = models.IntegerField(default=1)
    #item3 = models.ForeignKey(item, on_delete=models.CASCADE,default=None)
    i3c = models.TextField(default=False)
    q3c = models.IntegerField(default=1)
    #item4 = models.ForeignKey(item, on_delete=models.CASCADE,default=None)
    i4c = models.TextField(default=False)
    q4c = models.IntegerField(default=1)
    #item5 = models.ForeignKey(item, on_delete=models.CASCADE,default=None)
    i5c = models.TextField(default=False)
    q5c = models.IntegerField(default=1)
    #item6 = models.ForeignKey(item, on_delete=models.CASCADE,default=None)
    i6c = models.TextField(default=False)
    q6c = models.IntegerField(default=1)


'''class transaction(models.Model):
    desc = models.TextField(default=None)
    date = models.DateField()
    amount = models.IntegerField(default=0)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)'''

class Provider(models.Model):
    name = models.TextField(primary_key=True)
    pcat = models.TextField(default = 'Electricity')

class Movie(models.Model):
    name = models.TextField(primary_key=True)
    cost = models.IntegerField(default = 100)

class Bus(models.Model):
    name = models.TextField(primary_key=True)
    cost = models.IntegerField(default = 100)
    starting = models.TextField(default = False)
    dest = models.TextField(default = False)

class TicketBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default=None)
    date = models.DateField(auto_now=True)
    seats = models.IntegerField(default=1)
    amount = models.IntegerField(default=0)

class TicketBookBus(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE, default=None)
    date = models.DateField(auto_now=True)
    seats = models.IntegerField(default=1)
    amount = models.IntegerField(default=0)
    
class Bill(models.Model):
    amount = models.IntegerField(default=0)
    phone = models.IntegerField(primary_key=True)

class Promo(models.Model):
    name = models.TextField(primary_key=True)
    perc = models.IntegerField(default=0)