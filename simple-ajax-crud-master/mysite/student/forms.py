from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'roll_no', 'dob', 'adhar_number', 'mobile_number', 'blood_group', )
