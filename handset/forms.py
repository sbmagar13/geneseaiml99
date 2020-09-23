from django import forms
from django.forms import PasswordInput

from handset.models import Handset


class HandsetForm(forms.ModelForm):
    class Meta:
        model = Handset
        fields = ['PhoneNo', 'Password', 'confirmPassword', 'MacAddress', 'ManagerName', 'ManagerPhoneNo', 'Department',
                  'FinalApprover']
        labels = {'PhoneNo': 'Phone ID No.',
                  'Password': 'Password',
                  'confirmPassword': 'Confirm Password',
                  'MacAddress': 'MAC Address',
                  'ManagerName': 'Manager Name',
                  'ManagerPhoneNo': 'Manager Phone No.',
                  'Department': 'Department',
                  'FinalApprover': 'Final Approver Key',
                  }
        widgets = {
            'Password': PasswordInput(),
            'confirmPassword': PasswordInput(),
        }


class ApproverForm(forms.Form):
    approver_key = forms.CharField(required=True, label='Approver Key')
