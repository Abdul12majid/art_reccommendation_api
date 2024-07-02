from django.contrib import admin
from .models import A_or_U, Profile
from django.contrib.auth.models import Group, User

# Register your models here.
admin.site.unregister(Group)
admin.site.register(A_or_U)


class ProfileInline(admin.StackedInline):
	model=Profile

class UserAdmin(admin.ModelAdmin):
	model=User
	fields=('first_name', 'last_name', 'username', 'email',)
	list_display=('username', 'email',) 
	inlines=[ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
