from django.db import models
import uuid
from buyers.models import *
# Create your models here.

class Car(models.Model):
    namacar = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    buyer = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    code = models.CharField(max_length=10,blank=True)
    
    def __str__(self):
        return f"{self.namacar}-{self.price}-{self.buyer}"
    
    
    #?With default Django save function
    # def save(self,*args,**kwargs):
    #     if self.code == '':
    #         self.code = str(uuid.uuid4()).replace('-','').upper()[:10]
    #     return super().save(*args,**kwargs)