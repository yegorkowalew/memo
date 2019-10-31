from django.contrib import admin

from .models import DocumentDate

@admin.register(DocumentDate)
class DocumentDateAdmin(admin.ModelAdmin):
    pass