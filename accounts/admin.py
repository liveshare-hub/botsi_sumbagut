from django.contrib import admin

from .models import Bidang, UserAccount

admin.site.register(Bidang)


class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'name', 'bidang',
                    'email', 'is_staff', 'is_kabid')
    list_display_links = ('id', 'username')
    search_fields = ('username', 'name', 'bidang', 'email',)


admin.site.register(UserAccount, UserAccountAdmin)
