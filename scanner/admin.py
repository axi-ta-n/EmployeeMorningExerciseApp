from django.contrib import admin
from .models import Employee, ScanRecord
from import_export import resources
from import_export.admin import ImportExportModelAdmin 

class ScanRecordResource(resources.ModelResource):
    class Meta:
        model = ScanRecord
        fields = ('employee__employee_id', 'employee__name', 'employee__department', 'scan_time', 'status',)
        export_order = ('employee__employee_id', 'employee__name', 'employee__department', 'scan_time', 'status',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'department')
    search_fields = ('employee_id', 'name', 'department')

@admin.register(ScanRecord)
class ScanRecordAdmin(ImportExportModelAdmin): 
    resource_class = ScanRecordResource 
    list_display = ('employee', 'scan_time', 'status')
    list_filter = ('status', 'scan_time')
    date_hierarchy = 'scan_time'
    list_per_page = 100 