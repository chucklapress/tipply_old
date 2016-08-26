from django.contrib import admin
from app.models import EmployeeListing, Employee, WorkSkill

# Register your models here.
admin.site.register(EmployeeListing)
admin.site.register(Employee)
admin.site.register(WorkSkill)
