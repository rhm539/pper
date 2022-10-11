from django.contrib import admin

from setup.models import *
##


class buyerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'shortcut', 'address')


class styleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'buyer', 'smv')
    list_filter = ('name', 'buyer', 'smv')


# Register your models here.
admin.site.register(buyer, buyerAdmin)
admin.site.register(style, styleAdmin)
