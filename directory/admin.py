from django.utils.html import format_html
from .models import *
from django.contrib import admin
from django.conf import settings
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    def picture(self, obj):
        return format_html(f'<img width="200" src="{settings.MEDIA_URL}{obj.img}">')

    picture.allow_tags = True
    list_display = ('title', 'picture')


admin.site.register(Category, ProductAdmin)
admin.site.register(Item, ProductAdmin)
