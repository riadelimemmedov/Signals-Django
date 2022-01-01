from django.db.models.signals import pre_save
from django.dispatch import receiver
from buyers.models import *
import uuid
from .models import *


@receiver(pre_save,sender=Car)
def pre_save_code_and_modify_buyer(sender,instance,**kwargs):
    if instance.code == '':
        instance.code = str(uuid.uuid4()).replace('-','').upper()[:10]
        
    obj = Buyer.objects.get(userbuyer=instance.buyer.userbuyer)
    obj.from_signal = True
    obj.save()