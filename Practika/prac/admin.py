from django.contrib import admin
from .models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['id', 'userName', 'userPass', 'userRole']

admin.site.register(User, UserAdmin)