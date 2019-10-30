from django.contrib import admin

# Register your models here.
from .models import OfficeNote, Couterparty, Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Couterparty)
class CouterpartyAdmin(admin.ModelAdmin):
    pass


@admin.register(OfficeNote)
class OfficeNoteAdmin(admin.ModelAdmin):
    pass
