from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
phone_validator = RegexValidator(
    regex=r'^\+?\d{10,15}$',
    message="Phone number must be 10 to 15 digits and can start with '+'"
)


class StudentProfile(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=20, validators=[phone_validator], blank=True, null=True)

    # Address Information
    address_line = models.CharField(max_length=255, default='N/A')
    city = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.PositiveIntegerField(blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    citizenship = models.CharField(max_length=100, blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    current_location = models.CharField(max_length=100, blank=True, null=True)

    # Family Information
    guardian_contact = models.CharField(max_length=20, validators=[phone_validator], blank=True, null=True)
    guardian_relation = models.CharField(max_length=100, blank=True, null=True)
    cities_lived = models.PositiveIntegerField(blank=True, null=True)
    father_profession = models.CharField(max_length=100, blank=True, null=True)
    mother_profession = models.CharField(max_length=100, blank=True, null=True)
    family_income = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    sibling_name = models.CharField(max_length=100, blank=True, null=True)
    sibling_age = models.PositiveIntegerField(null=True, blank=True)
    sibling_institution = models.CharField(max_length=255, blank=True, null=True)
    abroad_details = models.TextField(blank=True, null=True)