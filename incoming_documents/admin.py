from django.contrib import admin

from .models import DocumentDate, DocumentMust

@admin.register(DocumentDate)
class DocumentDateAdmin(admin.ModelAdmin):
    pass

@admin.register(DocumentMust)
class DocumentMustAdmin(admin.ModelAdmin):
    pass