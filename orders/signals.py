from django.db.models.signals import m2m_changed,post_save
from django.dispatch import receiver
from sales.models import *
from .models import *

@receiver(m2m_changed,sender=Order.cars.through)
def m2m_changed_cars_order_total_total_price(sender,instance,action,**kwargs):
    
    print('Running')
    print(action)
    
    total_car = 0
    total_price = 0
    if action == 'post_add' or action == 'post_remove':
        print('Work')
        print(action)
        for car in instance.cars.all():
            total_car += 1
            total_price += car.price

        instance.total_car = total_car
        instance.total_price = total_price
        instance.save()#yeni Order.save() seklinde 
        

@receiver(post_save,sender=Order)
def post_save_create_or_update_sale(sender,instance,created,**kwargs):
    obj,_ = Sale.objects.get_or_create(order=instance)
    obj.amount = instance.total_price
    obj.save()
    
