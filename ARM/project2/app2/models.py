from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from datetime import datetime


# Create your models here.
# class Ignitz(models.Model):
#     Candidate_Name=models.CharField(max_length=100)
#     Father_Name=models.CharField(max_length=100)
#     Referred_By=models.CharField(max_length=100)
#     Date_Of_Birth=models.DateField()
#     Mobile_number=models.IntegerField()
#     Email_Id=models.EmailField()
#     Hometown=models.CharField(max_length=100)
#     Qualification=models.CharField(max_length=50)
#     College_name=models.CharField(max_length=100)
#     Stream=models.CharField(max_length=50)
#     Btech_Percentage=models.IntegerField()
#     Passed_out_year=models.IntegerField()
#     Any_Backlogs=models.CharField(max_length=100)

def validate_mobile_number(value):
    mobile_number_str = str(value)
    if len(mobile_number_str) < 10:
        raise ValidationError('Mobile number must have at least 10 digits.')


class Ignitz(models.Model):
    Candidate_Name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    Father_Name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    Referred_By = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    Date_Of_Birth = models.DateField()
    Mobile_Number = models.BigIntegerField(default=0,validators=[validate_mobile_number])
    Email_Id = models.EmailField()
    Hometown = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    Qualification = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    College_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    Stream = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    Btech_Percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    Passed_out_year = models.PositiveIntegerField()
    Any_Backlogs = models.CharField(max_length=100, validators=[MinLengthValidator(0)])

    def __str__(self):
        return self.Candidate_Name


# class Attendance(models.Model):
#     Student_Id=models.IntegerField()
#     Student_Names=models.CharField(max_length=100)
#     # Present_Date=models.DateField()
#     Present_Date = models.DateField(null=True, blank=True)
#     Status=models.CharField(max_length=100)


class Attendance(models.Model):
    Student_Id = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999999)]
    )
    Student_Names = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    # Present_Date = models.DateField()
    Present_Date = models.DateField(null=True, blank=True)
    Status = models.CharField(
        max_length=100,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
            ('Excused', 'Excused'),
        ]
    )

    def __str__(self):
        return self.Student_Names


class Login(models.Model):
    username=models.EmailField()
    password=models.CharField(max_length=100)
class StudentPassword(models.Model) :
    username=models.CharField(max_length=20)  
    password=models.CharField(max_length=30)
    confim_password=models.CharField(max_length=30)
    def __str__(self):
        return self.username
# class StdLogin(models.Model) :
#     username=models.CharField(max_length=20)  
#     password=models.CharField(max_length=30)