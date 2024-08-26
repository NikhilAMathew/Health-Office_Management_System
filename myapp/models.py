
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
 
# Create your models here.
departments = [('Cardiologist', 'Cardiologist'),
               ('Dermatologists', 'Dermatologists'),
               ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
               ('Allergists/Immunologists', 'Allergists/Immunologists'),
               ('Anesthesiologists', 'Anesthesiologists'),
               ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
               ]


def mobile(value):
    if value.isnumeric() and len(value) == 10:
        pass
    else:
        raise ValidationError(_('%(value)s is not a valid number'), params={'value': value}, )
id_proofs = [ 
    ('Aadhar card', 'Aadhar card'),
    ('PAN Card', 'PAN Card'),
    ('Driving licence', 'Driving licence'),
]

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    mobile = models.CharField(max_length=10, null=True, validators=[mobile])
    
    profile_pic = models.ImageField(upload_to='profile_pic/DoctorProfilePic/', null=True, blank=True)
    id_type = models.CharField(max_length=30, choices=id_proofs)
    id_proof = models.FileField(upload_to='id_proofs')
    address = models.TextField(default=" ")
    
   
    



    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, choices=[
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Others', 'Others'),
    ])
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=10, null=True, validators=[mobile])
    dob = models.DateField(verbose_name='Date of birth')
    address = models.TextField(default=" ")
   
    profile_pic = models.ImageField(upload_to='profile_pic/customerProfilePic/', null=True, blank=True)
    id_type = models.CharField(max_length=30, choices=id_proofs)
    id_proof = models.FileField(upload_to='id_proofs', default=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Lab(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lab_name = models.CharField(max_length=20, null=True)
    address = models.TextField(default=" ")
    
    mobile = models.CharField(max_length=10, null=True, validators=[mobile])
    # id_type = models.CharField(max_length=30, choices=id_proofs)
    id_proof = models.FileField(verbose_name='Registration document', upload_to='id_proofs')

    def __str__(self):
        return self.lab_name


class HI(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    profile_pic = models.ImageField(upload_to='profile_pic/HIProfilePic/', null=True, blank=True)
    dob = models.DateField(verbose_name='Date of birth')
    address = models.TextField(default=" ")
    
    mobile = models.CharField(max_length=10, null=True, validators=[mobile])
    id_type = models.CharField(max_length=30, choices=id_proofs)
    id_proof = models.FileField(upload_to='id_proofs')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
import datetime
def validate_date(value):
    for i in Appointment.objects.all():
        now = i.date_of_appointment
        # utc = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
        utc = value
        # now = datetime.datetime.now()
        time_delta = now-utc
        seconds= time_delta.total_seconds()
        minutes = seconds/60
        print('minutes:',minutes)
        if 0<=minutes<=15 or 0>=minutes>=-15:
            raise ValidationError(_('Slot for this time is already booked,Try after 30 minutes'), params={'value': value}, )
        else:pass
from django.core.exceptions import ValidationError
class Appointment(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    symptoms = models.TextField()
    date = models.DateField(auto_now=True)
    date_of_appointment = models.DateTimeField(validators=[validate_date])
    # def save(self):
    #     if self.date_of_appointment < datetime.datetime.now():
    #         raise ValidationError('Error occured')

    def __str__(self):
        return f'{self.patient} ({self.doctor})'


tes = '''Blood pressure
Blood sugar
Cholesterol'''.split('\n')
tes = [(i, i) for i in tes]
tests = [('Cardiologist', 'Cardiologist'),
         ('Dermatologists', 'Dermatologists'),
         ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'),
         ('Allergists/Immunologists', 'Allergists/Immunologists'),
         ('Anesthesiologists', 'Anesthesiologists'),
         ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')
         ]


class LabBooking(models.Model):
    patient = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    test = models.CharField(max_length=50, choices=tes)
    # symptoms = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.patient} ({self.test})'

class Daily_booking_limit(models.Model):
    limit = models.IntegerField()
    date = models.DateField(auto_now=True, unique=True)

    def __str__(self):
        return str(self.date)

class LabReport(models.Model):
    patient = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE, null=True, blank=True, help_text='Specify if any ')
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    report = models.FileField(upload_to='lab_reports')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.patient} ({self.lab})'


s = 'Polio,Typhoid,Chicken pox,Hepatitis'.split(',')
v = [(i, i) for i in s]


class VaccineDate(models.Model):
    date = models.DateTimeField()
    vaccine = models.CharField(choices=v, default='Polio', max_length=20)

    def __str__(self):
        return self.date


class PrescriptionsToLab(models.Model):
    patient = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    # prescription = models.FileField(upload_to='lab_reports', null=True, blank=True)
    prescription = models.TextField(default=' ')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.patient} ({self.lab})'
class VaccancyLimit(models.Model):
    limit = models.IntegerField(default=0)
job_types = [ 
    ('samplejob', 'sample_job'),
    ('samplejob', 'sample_job'),
    ('samplejob', 'sample_job'),
    ('samplejob', 'sample_job'),
]
class Jobs(models.Model):
    title = models.CharField(max_length=50)
    vaccancies = models.IntegerField(default=1)
    description = models.TextField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.title}'
        
class VacancyApply(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(verbose_name='Date of birth', help_text='DD/MM/YYYY')
    mobile = models.CharField(max_length=10, validators=[mobile])
    address = models.TextField(default=" ")
    
    preference = models.ForeignKey(Jobs, limit_choices_to={'active':True}, on_delete=models.CASCADE)
    email = models.EmailField()
    bio_data = models.FileField(upload_to='bio_data')

    def __str__(self):
        return self.first_name


class Review(models.Model):
    user = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300, verbose_name='Feedback')