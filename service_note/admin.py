from django.contrib import admin
from .models import ServiceNote, OperativeNote, ReadyOrder, InDocument, Waybill, SheduleFile, SheduleFileError, Shedule


class ServiceNoteAdmin(admin.ModelAdmin):
    list_display = (['product_name', 'counterparty', 'order_no', 'in_id'])

# class OperativeNoteAdmin(admin.ModelAdmin):
#     list_display = (['product_name', 'counterparty', 'pickup_plan_date', 'shipping_plan_date'])


class WaybillAdmin(admin.ModelAdmin):
    list_display = (['document', 'number', 'order_no'])


class ReadyOrderAdmin(admin.ModelAdmin):
    list_display = (['in_id', 'ready', 'ready_date'])


class InDocumentAdmin(admin.ModelAdmin):
    # pass
    list_display = (['in_id',
                     'dispatcher',
                     'pickup_issue',
                     # 'pickup_date_1',
                     # 'pickup_date_2',
                     # 'pickup_date_3',
                     'shipping_issue',
                     # 'shipping_date_1',
                     # 'shipping_date_2',
                     # 'shipping_date_3',
                     'design_issue',
                     # 'design_date_1',
                     # 'design_date_2',
                     # 'design_date_3',
                     'drawings_issue',
                     # 'drawings_date_1',
                     # 'drawings_date_2',
                     # 'drawings_date_3'
                     ])

# class SheduleFile(admin.ModelAdmin):
#     pass


admin.site.register(ServiceNote, ServiceNoteAdmin)
# admin.site.register(OperativeNote, OperativeNoteAdmin)
admin.site.register(ReadyOrder, ReadyOrderAdmin)
admin.site.register(InDocument, InDocumentAdmin)
admin.site.register(Waybill, WaybillAdmin)
admin.site.register(SheduleFile)
admin.site.register(SheduleFileError)
admin.site.register(Shedule)
