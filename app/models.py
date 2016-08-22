from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

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
