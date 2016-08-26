from django.contrib import admin
from app.models import EmployeeListing, Employee, WorkSkills

# Register your models here.
admin.site.register(EmployeeListing)
admin.site.register(Employee)
admin.site.register(WorkSkills)
