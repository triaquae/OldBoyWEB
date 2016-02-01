from django.contrib import admin

# Register your models here.

import models

class NotificationLinksAdmin(admin.ModelAdmin):
    list_display=('priority', 'category','title','hide','date','class_open_date')
    list_editable = ('hide','class_open_date')
admin.site.register(models.NotificationLinks,NotificationLinksAdmin)