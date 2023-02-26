from django.contrib import admin
# Register your models here.
from flowershopapp.models import Flowers


class FlowerAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Flowers,FlowerAdmin)