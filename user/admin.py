from django.contrib import admin
from .models import UserCart,UserFavourite
# Register your models here.
admin.site.register(UserCart)
admin.site.register(UserFavourite)
