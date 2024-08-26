from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.HI)
admin.site.register(models.Lab)
admin.site.register(models.CustomerProfile)
admin.site.register(models.DoctorProfile)
admin.site.register(models.Appointment)
admin.site.register(models.LabBooking)
admin.site.register(models.LabReport)
admin.site.register(models.VacancyApply)
admin.site.register(models.Review)
admin.site.register(models.Daily_booking_limit)
admin.site.register(models.VaccancyLimit)