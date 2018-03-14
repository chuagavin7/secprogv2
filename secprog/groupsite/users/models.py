from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    contact_num = models.CharField(null=True, max_length=20)
    billingAdd = models.CharField(null=False, max_length=1024)
    shippingAdd = models.CharField(null=False, max_length=1024)
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
    
class PurchaseHistory(models.Model):
    def method():
        from posts.models import Item
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        item = models.ForeignKey(Item, on_delete=models.CASCADE)

class AdminUser(models.Model):
    uname = models.CharField(null=False, max_length=150)
    password = models.CharField(null=False, max_length=150)
    typeof = models.IntegerField(default=0)