from django.contrib import admin
from .models import PurchaseHistory, Profile, AdminUser

# Register your models here.
admin.site.register(Profile)
admin.site.register(PurchaseHistory)
admin.site.register(AdminUser)