from django.contrib import admin
from setup.models import Department, unit, userType

from user.models import Profile

#


class unitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'shortcut', 'address')


# Register your models here.
admin.site.register(Profile)
admin.site.register(Department)
admin.site.register(userType)
admin.site.register(unit, unitAdmin)
