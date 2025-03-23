from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Msg


class MsgAdmin(admin.ModelAdmin):
    list_display = ('sensor_name', 'slug', 'time', 'value')
    list_filter = ('time',)
    search_fields = ('sensor_name', 'description')
    prepopulated_fields = {'slug': ('sensor_name',)}


admin.site.register(Msg, MsgAdmin)
