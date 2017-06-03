from django.contrib import admin

# Register your models here.
from .models import Room_info, Option_info, Address

admin.site.register(Room_info)
admin.site.register(Option_info)
admin.site.register(Address)
