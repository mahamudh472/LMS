from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shift = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    roll = models.CharField(max_length=50, blank=True, null=True, default="000000")
    name_bangla = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True, default="")
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    post_office = models.CharField(max_length=50, blank=True, null=True)
    upazila = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=50, blank=True, null=True)
    parent_number = models.CharField(max_length=50, blank=True, null=True)
    blood_group = models.CharField(max_length=50, blank=True, null=True)
    technology_code = models.CharField(max_length=50, blank=True, null=True)
    semester = models.CharField(max_length=50, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    ssc_roll = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to="student", null=True, blank=True)
    signature = models.ImageField(upload_to="signature", null=True, blank=True)
    parent_signature = models.ImageField(upload_to="signature", null=True, blank=True)
    policy_agreement = models.BooleanField(default=True)

    is_active = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
