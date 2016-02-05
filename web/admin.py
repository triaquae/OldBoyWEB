from django.contrib import admin

# Register your models here.

import models

class NotificationLinksAdmin(admin.ModelAdmin):
    list_display=('priority', 'category','title','hide','date','class_open_date')
    list_editable = ('hide','class_open_date')

class NewGraduatesAdmin(admin.ModelAdmin):
    list_display = ('course_name','semester','graduate_date')
class PublicClassAdmin(admin.ModelAdmin):
    list_display = ["title","start_date","teacher","img"]
admin.site.register(models.NotificationLinks,NotificationLinksAdmin)
admin.site.register(models.PublicClass,PublicClassAdmin)
admin.site.register(models.NewGraduates,NewGraduatesAdmin)