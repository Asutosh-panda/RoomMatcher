from django.contrib import admin
from .models import Hostelite,Register
# Register your models here.

class HosteliteAdmin(admin.ModelAdmin):
    list_display = ('sic','first_name','last_name','year')
    search_fields = ('sic','first_name','last_name')

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('sic',)
    search_fields = ('sic',)

admin.site.register(Hostelite,HosteliteAdmin)
admin.site.register(Register,RegisterAdmin)

