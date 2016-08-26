from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



# Create your models here.

class EmployeeListing(models.Model):
    applicant_name = models.CharField(max_length=50)
    applicant_email = models.EmailField(max_length=30)
    applicant_phone = models.IntegerField(unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    position_applying_for = models.CharField(max_length=80)
    date_applying = models.DateTimeField(auto_now_add=True)
    post_resume_or_cover = models.TextField(max_length=None)

    def __str__(self):
        return self.applicant_name

@receiver(post_save, sender="auth.User")
def create_token(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Token.objects.create(user=instance)

class Employee(models.Model):
    employee_name = models.CharField(max_length=50)
    dob = models.DateField(max_length=8)
    address = models.TextField(max_length=None)
    telephone_number = models.IntegerField(unique=True, validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    federal_and_state_filling_status = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    start_date = models.DateField(max_length=8)
    end_date = models.DateField(max_length=8)
    recieved_employee_handbook = models.BooleanField(default=True)
    personel_notes = models.TextField(max_length=None)
    def __str__(self):
        return self.employee_name

class WorkSkills(models.Model):
    appearence = models.IntegerField()
    customer_skills = models.IntegerField()
    team_work = models.IntegerField()
    adhere_company_policies = models.IntegerField()
    accepts_coaching = models.IntegerField()
    self_starting = models.IntegerField()
    employee_name = models.CharField(max_length=50)
    employee_number = models.ForeignKey(Employee)
    def __str__(self):
        return self.employee_name
