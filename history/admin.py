from django.contrib import admin

from .models import History, IconType


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    pass


@admin.register(IconType)
class IconTypeAdmin(admin.ModelAdmin):
    pass
