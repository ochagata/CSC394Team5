from Pazzos.models import PazzosUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(PazzosUser)

class PazzosUserInline(admin.StackedInline):
    model = PazzosUser
    can_delete = False
    
class UserAdmin(UserAdmin):
    inlines = (PazzosUserInline, )
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)