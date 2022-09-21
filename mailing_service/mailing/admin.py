from django.contrib import admin

from .models import Mailing, Client, Message


# @admin.register(Mailing)
# class MailingAdmin(admin.ModelAdmin):
#
#     list_display = ('text', )
admin.site.register(Mailing)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'mobile_code', 'tag', 'timezone')


admin.site.register(Message)
