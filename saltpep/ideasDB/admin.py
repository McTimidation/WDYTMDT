from django.contrib import admin
from .models import CustomUser, Outing

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser



admin.site.register(Outing)
admin.site.register(CustomUser, CustomUserAdmin)
