from django.contrib import admin

from apps.models import Blog


# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass