from django.contrib import admin
from websites.models import WebSite


class WebSiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

admin.site.register(WebSite, WebSiteAdmin)
