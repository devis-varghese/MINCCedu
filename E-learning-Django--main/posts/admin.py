from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.

class CuricullamAdmin(admin.StackedInline):
    model = Curriculam
 
class featuresAdmin(admin.StackedInline):
    model = features


class timeAdmin(admin.StackedInline):
    model = timing


class videoAdmin(admin.StackedInline):
    model = video
 
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CuricullamAdmin,timeAdmin, videoAdmin]
 
    class Meta:
       model = Post



@admin.register(Curriculam)
class CuricullamAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered']


admin.site.register(Category)

admin.site.register(MainCourse)
admin.site.register(enrolledstudents)

admin.site.register(Order, OrderAdmin)
admin.site.register(passedstudents)
admin.site.register(subcat)



