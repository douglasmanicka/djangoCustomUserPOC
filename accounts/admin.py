from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .models import Account
admin.site.register(Account, auth_admin.UserAdmin)
