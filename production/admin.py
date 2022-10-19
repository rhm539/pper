from django.contrib import admin

from production.models import production

# Register your models here.


class productionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'planID', 'plan', 'sewingDate')


admin.site.register(production, productionAdmin)
