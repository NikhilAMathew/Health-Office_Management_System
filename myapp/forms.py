from django.contrib.auth.forms import forms
from django.db.models import fields
from . import models
import datetime


class DoctorForm(forms.ModelForm):
    dob = forms.DateField(label='Date of birth',
                          widget=forms.DateInput(attrs={'type': 'date', 'max':'2015-02-20'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))

    class Meta:
        model = models.DoctorProfile
        exclude = ['user']

class JobsForm(forms.ModelForm):
    class Meta:
        model = models.Jobs
        exclude = ['active']

class CustomerForm(forms.ModelForm):
    dob = forms.DateField(label='Date of birth',
                          widget=forms.DateInput(attrs={'type': 'date', 'max':'2015-02-20'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))

    class Meta:
        model = models.CustomerProfile
        exclude = ['user']


class LabForm(forms.ModelForm):
    lab_name = forms.CharField(widget=forms.TextInput(
        attrs={'autofocus': 'autofocus'}))

    class Meta:
        model = models.Lab
        exclude = ['user']


class HIForm(forms.ModelForm):
    dob = forms.DateField(label='Date of birth',
                          widget=forms.DateInput(attrs={'type': 'date', 'max':'2015-02-20'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))

    class Meta:
        model = models.HI
        exclude = ['user']

import datetime
class VaccineDateForm(forms.ModelForm):
    # date = forms.DateTimeField(label='Vaccine date', widget=forms.DateTimeInput(attrs={
    #     'type': 'datetime-local',

    # }))
    date = forms.DateTimeField(label='Vaccine date',
                          widget=forms.DateTimeInput(attrs={'type': 'datetime-local','min':datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')}
                          ))
    class Meta:
        model = models.VaccineDate
        fields = '__all__'


class PrescriptionsToLabForm(forms.ModelForm):
    class Meta:
        model = models.PrescriptionsToLab
        exclude = ['doctor']


class VacancyApplyForm(forms.ModelForm):
    dob = forms.DateField(label='Date of birth',
                          widget=forms.DateInput(attrs={'type': 'date', 'max':'2015-02-20'}))
    class Meta:
        model = models.VacancyApply
        fields = '__all__'

class VaccancyLimitForm(forms.ModelForm):
    class Meta:
        model = models.VaccancyLimit
        fields = '__all__'

d = datetime.datetime.now().strftime('%d')

class AppointmentForm(forms.ModelForm):
    date_of_appointment = forms.DateTimeField(label='Date of appointment',
                          widget=forms.DateTimeInput(attrs={'type': 'datetime-local','min':datetime.datetime.now().strftime('%Y-%m-%dT%H:%M'),
                         'max':datetime.datetime.now().strftime(f'%Y-%m-{d}T%H:%M')}
                          ))
    class Meta:
        model = models.Appointment
        exclude = ['patient']


class LabBookingForm(forms.ModelForm):
    date = forms.DateTimeField(label='Date of appointment',
                          widget=forms.DateTimeInput(attrs={'type': 'datetime-local','min':datetime.datetime.now().strftime('%Y-%m-%dT%H:%M'),
                          'max':datetime.datetime.now().strftime(f'%Y-%m-{d}T%H:%M')}
                          ))
    class Meta:
        model = models.LabBooking
        exclude = ['patient']


class LabReportForm(forms.ModelForm):
    class Meta:
        model = models.LabReport
        exclude = ['lab']


class ReviewForm(forms.ModelForm):
    comment= forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}), label='Feedback')
   
    class Meta:
        model = models.Review
        exclude = ['user']
