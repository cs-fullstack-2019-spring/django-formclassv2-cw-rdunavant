from django import forms
class EmployeeApplication(forms.Form):
    name = forms.CharField()
    birthDate = forms.DecimalField()
    position = forms.CharField()
    salary = forms.DecimalField()