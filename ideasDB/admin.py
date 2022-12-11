from django.contrib import admin
from .models import CustomUser, Outing, Activity

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser



admin.site.register(Outing)
admin.site.register(Activity)
admin.site.register(CustomUser, CustomUserAdmin)
