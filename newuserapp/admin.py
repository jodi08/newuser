from django.contrib import admin

from newuserapp.models import New_User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(New_User, UserAdmin)
