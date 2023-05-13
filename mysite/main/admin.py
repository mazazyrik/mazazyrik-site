from django.contrib import admin

from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'text',
        'email',
    )


admin.site.register(Contact, ContactAdmin)
