from django.contrib import admin
from .models import CustomUser, Social

# Register your models here.


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    readonly_field = ('placed')
admin.site.register(Social)


admin.site.site_header = "Roomege Admin Portal"
admin.site.site_title = "Roomege Admin Portal" 
admin.site.index_title = "Welcome to the Roomege Admin Portal!" 