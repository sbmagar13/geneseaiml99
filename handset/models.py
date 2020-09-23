from django.db import models
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from .validators import validate_MAC
from phone_field import PhoneField


class Handset(models.Model):
    PhoneNo = models.IntegerField()
    Password = models.CharField(validators=[MinLengthValidator(8)], max_length=100)
    confirmPassword = models.CharField(max_length=100)
    MacAddress = models.CharField(validators=[validate_MAC], max_length=20,
                                  default='aa:bb:cc:dd:ee:ff')
    ManagerName = models.CharField(max_length=100)
    ManagerPhoneNo = PhoneField(blank=True)
    Department = models.CharField(max_length=100)
    FinalApprover = models.CharField('Final Approver', max_length=100, null=False)

    def clean(self):
        if self.Password != self.confirmPassword:
            raise ValidationError('Passwords are not equal')
        password_validation.validate_password(self.Password, None)
        return self.Password
