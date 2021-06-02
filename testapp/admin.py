from django.contrib import admin
from testapp.models import Location,Theatre
# Register your models here.




class LocationAdmin(admin.ModelAdmin):
    list_display=['location']

admin.site.register(Location,LocationAdmin)

class TheatreAdmin(admin.ModelAdmin):
    list_display=['theatre']

admin.site.register(Theatre,TheatreAdmin)
