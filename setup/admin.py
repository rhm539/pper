from django.contrib import admin

from setup.models import *
##


class unitAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortcut', 'address')


class buyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'shortcut', 'address')


class styleAdmin(admin.ModelAdmin):
    list_display = ('name', 'buyer', 'smv')
    list_filter = ('name', 'buyer', 'smv')


# Register your models here.
admin.site.register(Department)
admin.site.register(userType)
admin.site.register(unit, unitAdmin)
admin.site.register(buyer, buyerAdmin)
admin.site.register(style, styleAdmin)
