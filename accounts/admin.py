from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import AccountChangeForm, AccountCreationForm
from .models import Account

@admin.register(Account)
class AccountAdmin(auth_admin.UserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    model = Account
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Profile", {"fields": ("type",)}),
    )

    
#admin.site.register(Account, auth_admin.UserAdmin)
