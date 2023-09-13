from django.contrib import admin

from core_apps.profiles import models
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pkid", "id", "username", "country", "gender"]
    list_display_links = ["pkid", "id"]
    list_filter = ["gender"]
    search_fields = ["username", "country", "user__phone"]
    
    @admin.display(ordering="user__phone")
    def user_phone(self, obj):
        return obj.user.phone
    
admin.site.register(models.Profile, ProfileAdmin)