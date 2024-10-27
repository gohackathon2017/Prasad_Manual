from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *
from django.contrib import admin

class Phase2StudentResource(resources.ModelResource):
    class Meta:
        model = Phase2Student
        fields = ('roll_no', 'name', 'fathers_name', 'student_mobile', 'father_mobile', 'email')
        import_id_fields = ['roll_no']

@admin.register(Phase2Student)
class Phase2StudentAdmin(ImportExportModelAdmin):
    resource_class = Phase2StudentResource
    list_display = ('roll_no', 'name', 'fathers_name', 'student_mobile', 'father_mobile', 'email')
    search_fields = ('roll_no', 'name', 'email')