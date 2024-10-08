from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/<type>', views.signup, name='signup'),
    path('user_login', views.user_login, name='user_login'),
    path('customer_profile', views.customer_profile, name='customer_profile'),
    path('doctor_profile', views.doctor_profile, name='doctor_profile'),
    path('HI_profile', views.HI_profile, name='HI_profile'),
    path('lab_profile', views.lab_profile, name='lab_profile'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('appointment', views.appointment, name='appointment'),
    path('lab_booking', views.lab_booking, name='lab_booking'),
    path('lab_report', views.lab_report, name='lab_report'),
    path('lab_reports_view', views.lab_reports_view, name='lab_reports_view'),
    path('vaccine_date_form', views.vaccine_date_form, name='vaccine_date_form'),
    path('visited_patients', views.visited_patients, name='visited_patients'),
    path('lab_reports_hi', views.lab_reports_hi, name='lab_reports_hi'),
    path('prescriptions_to_lab', views.prescriptions_to_lab, name='prescriptions_to_lab'),
    path('vacancy_apply', views.vacancy_apply, name='vacancy_apply'),
    path('recruit', views.recruit, name='recruit'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('change_password', views.change_password, name='change_password'),
    path('select/<int:id>', views.select, name='select'),
    path('viewappointments', views.appointmentlist, name='viewappointments'),
    path('lablist', views.lablist, name='lablist'),
    path('deletelabs/<int:id>/', views.deletelabs, name='deletelabs'),
    path('deleteappointments/<int:id>/', views.deleteappointment, name='deleteappointment'),
    path('editappointment/<int:id>/', views.editappointment, name='editappointment'),
    path('editlabs/<int:id>/', views.editlabs, name='editlabs'),
    path('review', views.review, name='review'),
    path('reviewlist', views.reviewlist, name='reviewlist'),
    path('view_prescriptions', views.view_prescriptions, name='view_prescriptions'),
    path('updatevaccancy', views.updatevaccancy, name='updatevaccancy'),
    path('usertype', views.usertype, name='usertype'),
    path('adminindex/', views.adminindex, name='adminindex'),
    path('admin_patients/', views.admin_patients, name='admin_patients'),
    path('admin_doctors/', views.admin_doctors, name='admin_doctors'),
    path('admin_hi/', views.admin_hi, name='admin_hi'),
    path('admin_lab/', views.admin_lab, name='admin_lab'),
    path('admin_limit/', views.admin_limit, name='admin_limit'),
    path('admin_job/', views.admin_job, name='admin_job'),
    path('admin_jobs/', views.admin_jobs, name='admin_jobs'),
    path('admin_password/', views.admin_password, name='admin_password'),
]

