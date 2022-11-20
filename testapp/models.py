from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class Registration(AbstractUser):
    username=models.CharField(max_length=40,unique=True)
    first_name=models.CharField(max_length=60, null=True, blank=True) 
    last_name=models.CharField(max_length=60, null=True, blank=True)
    email=models.CharField(max_length=60,unique=True,verbose_name='email',null=True, blank=True)
    
    location=models.TextField(null=True,blank=True)
    gender=models.CharField(max_length=6,null=True,blank=True)
    profile_pic=models.ImageField(upload_to='image',null=True,blank=True)
    mobile_no=models.CharField(max_length=13)
    birth_place=models.CharField(max_length=30,null=True,blank=True)
    
    occupation=models.CharField(max_length=40,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username + " " + self.email
    
    
class RegisterLocation(models.Model):
    shop_name=models.CharField(max_length=100,help_text="Enter Location",blank=True,null=True)
    shop_image=models.ImageField(upload_to='images/shop_image/',help_text="Upload Shop Name",blank=True,null=True)
    def __str__(self):
        return str(self.shop_name)
    class Meta:
        verbose_name_plural='Register Location(3)'
    
    
    
class Shop(models.Model):
    user=models.ForeignKey(Registration,on_delete=models.CASCADE,)
    location=models.ForeignKey(RegisterLocation,related_name='RegisterLocation',on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    #category = models.ForeignKey(Category,on_delete=models.CASCADE)
    brand = models.CharField(max_length=100, default='john doe')
    isbn = models.CharField(max_length=13)
    qualities = models.CharField(max_length=60)
    price = models.IntegerField()
    stock = models.IntegerField()
    review = models.TextField()
    image = models.ImageField(upload_to='shop_photos')
    # created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_created']
    def __str__(self):
        return self.title
    
    
class Shop1(models.Model) :
    eno=models.IntegerField()
    
    ename=models.CharField(max_length=100, null=False)   
    elocation = models.CharField(max_length=100)
    
    ereview = models.FloatField()
    ediscount = models.CharField(max_length=50) 
    
    ephone = models.IntegerField(default=0)
    eaddress = models.CharField(max_length=100)
    

    
    
    def __str__(self):
         return '%s %s %s %s %s %s  ' %(self.ename,self.elocation,self.ereview,self.ediscount,self.ephone,self.eaddress)
    
    
    
    

    
    
    
    
