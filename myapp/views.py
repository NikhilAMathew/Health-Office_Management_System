import datetime
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models
from django.contrib.auth.models import User
from django.contrib import messages
def admin_password(request):
    users = User.objects.all()
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get('username'))
        p = request.POST.get('password')
        print(p)
        user.set_password(p)
        user.save()
        messages.success(request, f'Password changed')
    return render(request, 'admin_password.html', {'users':users})
def admin_patients(request):
    objects = models.CustomerProfile.objects.all()
    return render(request, 'admin_patients.html', {'objects':objects})

# def admin_jobs(request):
#     objects = models.Jobs.objects.all()
#     return render(request, 'admin_jobs.html', {'objects':objects})

def admin_doctors(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get('username'))
        if request.POST.get('state'):
            user.is_active = False
            user.save()
        else:
            user.is_active = True
            user.save()
    objects = models.DoctorProfile.objects.all()
    return render(request, 'admin_doctors.html', {'objects':objects})

def admin_hi(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get('username'))
        if request.POST.get('state'):
            user.is_active = False
            user.save()
        else:
            user.is_active = True
            user.save()
    objects = models.HI.objects.all()
    return render(request, 'admin_hi.html', {'objects':objects})
def admin_lab(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.POST.get('username'))
        if request.POST.get('state'):
            user.is_active = False
            user.save()
        else:
            user.is_active = True
            user.save()
    objects = models.Lab.objects.all()
    return render(request, 'admin_lab.html', {'objects':objects})
def admin_jobs(request):
    if request.method == 'POST':
        user = models.Jobs.objects.get(id=request.POST.get('username'))
        if request.POST.get('state'):
            user.active = False
            user.save()
        else:
            user.active = True
            user.save()
    objects = models.Jobs.objects.all()
    return render(request, 'admin_jobs.html', {'objects':objects})

def admin_limit(request):
    if request.method == 'POST':
        limit = request.POST.get('limit')
        print(limit)
        l = models.Daily_booking_limit.objects.all()[0]
        l.limit = limit
        l.save()
        messages.success(request, 'Limit set successful')
        return redirect('adminindex')
    return render(request, 'admin_limit.html')

def admin_job(request):
    form = forms.JobsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('admin_jobs')
    return render(request, 'admin_job.html',{'form':form})

def adminindex(request):
    return render(request, 'admin_index.html')

def find_user(request):
    d = {'c': False, 'h': False, 'd': False, 'l': False, 'unknown':False}
    if request.user.id in [i.user_id for i in models.CustomerProfile.objects.all()]:
        d['c'] = True
    elif request.user.id in [i.user_id for i in models.DoctorProfile.objects.all()]:
        d['d'] = True
        d['c'] = False
    elif request.user.id in [i.user_id for i in models.Lab.objects.all()]:
        d['l'] = True
        d['c'] = False
    elif request.user.id in [i.user_id for i in models.HI.objects.all()]:
        d['h'] = True
        d['c'] = False
        print(d)
    else:
        d['unknown']=True
        d['c'] = False
    return d

def usertype(request):
    return render(request, 'usertypes.html')

def index(request):
    try:
            limits = models.Daily_booking_limit.objects.get(date=datetime.date.today()).limit
    except:
            limits=10
    jobs = models.Jobs.objects.filter(active=True)
    context=find_user(request)
    try:
        lm = models.VaccancyLimit.objects.all()[0].limit
    except:
        lm = 'No'
    context.update({
        'today':str(datetime.date.today()),
        'available':limits-len(models.Appointment.objects.filter(
            date=str(datetime.date.today()))),
        'limit':lm,
        'jobs':jobs,

    })
    context.update(find_user(request))
    return render(request, 'index.html', context)


def signup(request, type):
    UserForm = UserCreationForm(request.POST or None)
    DoctorForm = forms.DoctorForm(request.POST or None, request.FILES or None)
    CustomerForm = forms.CustomerForm(
        request.POST or None, request.FILES or None)
    HIForm = forms.HIForm(request.POST or None, request.FILES or None)
    LabForm = forms.LabForm(request.POST or None, request.FILES or None)
    dict_forms = {
        'UserForm': UserForm,
        'DoctorForm': DoctorForm,
        'CustomerForm': CustomerForm,
        'HIForm': HIForm,
        'LabForm': LabForm,
    }
    form = dict_forms[str(type)]
    if request.method == 'POST':
        form = dict_forms[str(type)]
        print(form)
        if form.is_valid() and UserForm.is_valid():
            UserForm.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                instance = form.save(commit=False)
                instance.user = request.user
                if str(type)=='DoctorForm' or str(type)=='LabForm' or str(type)=='HIForm':
                    user.is_active = False
                    user.save()
                instance.save()
                logout(request)
                messages.success(request, 'Account created successfully')
                return redirect('user_login')
    return render(request, 'signup.html', {'UserForm': UserForm, 'form': form})


@login_required(login_url='user_login')
def appointment(request):
    if not find_user(request)['c']:
        return render(request, 'not_auth.html', {})
    form = forms.AppointmentForm(request.POST or None)
    if form.is_valid():
        i = form.save(commit=False)
        try:
            i.patient = request.user
            i.save()
            messages.success(request, f'Appointment success')
            return redirect(index)
        except:
            messages.warning(request, f'You have already taken appointment')
    return render(request, 'form_template.html', {'form': form})


all_models = {'HI_profile': models.HI.objects.all(),
              'lab_profile': models.Lab.objects.all(),
              'doctor_profile': models.DoctorProfile.objects.all(),
              'customer_profile': models.CustomerProfile.objects.all()}


def user_login(request):
    form = AuthenticationForm(request.POST or None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('adminindex')
            login(request, user)
            # return render(request, 'index.html', find_user(request))
            return redirect('index')

        return render(request, 'login.html', {'form': form,
                                              's': "Incorrect username or password",
                                              'm': True})
    return render(request, 'login.html', {'form': form})


@login_required(login_url='user_login')
def customer_profile(request):
    customer = models.CustomerProfile.objects.get(user_id=request.user.id)
    return render(request, 'index.html', find_user(request))


@login_required(login_url='user_login')
def doctor_profile(request):
    doctor = models.DoctorProfile.objects.get(user_id=request.user.id)
    return render(request, 'index.html', find_user(request))


@login_required(login_url='user_login')
def HI_profile(request):
    HI = models.HI.objects.get(user_id=request.user.id)
    return render(request, 'index.html', find_user(request))


@login_required(login_url='user_login')
def lab_profile(request):
    Lab = models.Lab.objects.get(user_id=request.user.id)
    return render(request, 'index.html', find_user(request))


def user_logout(request):
    logout(request)
    return redirect('index')


def email_check(user):
    return user.email.endswith('@example.com')


@login_required(login_url='user_login')
def appointment(request):
    if not find_user(request)['c']:
        return render(request, 'not_auth.html', {})
    form = forms.AppointmentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instant = form.save(commit=False)
            print(request.POST.get('date'))
            
            instant.patient = models.CustomerProfile.objects.get(
                user_id=request.user.id)
            # instant.save()
            print(datetime.datetime.today())
            obj = models.Appointment.objects.filter(
                date=str(datetime.datetime.today())[0:10])
            try:
                limits = models.Daily_booking_limit.objects.get(date=datetime.date.today()).limit
            except:
                limits=10
            if len(obj) < limits:
                j = models.CustomerProfile.objects.get(
                user_id=request.user.id)
                if (len(models.Appointment.objects.filter(date=str(datetime.datetime.today())[0:10],patient=j))<1):
                    instant.save()
                    messages.success(request, f'Appointment success')
                else:
                    messages.warning(request, f'You have already taken appointment')
                    return redirect(index)
            else:
                messages.info(request, f'Maximum appointments exeeded')
            return redirect(index)
    return render(request, 'form_template_appointment.html', {'form': form})


@login_required(login_url='user_login')
def lab_booking(request):
    if not find_user(request)['c']:
        return render(request, 'not_auth.html', {})
    form = forms.LabBookingForm(request.POST or None)
    u = models.CustomerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        instant = form.save(commit=False)
        instant.patient_id = u.id
        instant.save()
        messages.success(request, f'Appointment success')
        return redirect(index)
    return render(request, 'form_template_lab_booking.html', {'form': form})


@login_required(login_url='user_login')
def lab_report(request):
    if not find_user(request)['l']:
        return render(request, 'not_auth.html', {})
    form = forms.LabReportForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        instant = form.save(commit=False)
        instant.lab_id = models.Lab.objects.get(user_id=request.user.id).id
        instant.save()
        messages.success(request, f'Report submit success')
        return redirect(index)
    patients = models.CustomerProfile.objects.all()
    return render(request, 'form_template_send_lab_report.html', {'form': form, 'patients':patients})


@login_required(login_url='user_login')
def lab_reports_view(request):
    if not (find_user(request)['c'] or find_user(request)['d']):
        return render(request, 'not_auth.html', {})
    if find_user(request)['d']:
        dprofile = models.DoctorProfile.objects.get(user_id=request.user.id)
        reports = models.LabReport.objects.filter(doctor_id=dprofile.id)
    else:
        cprofile = models.CustomerProfile.objects.get(user_id=request.user.id)
        reports = models.LabReport.objects.filter(patient_id=cprofile.id)
    return render(request, 'reports.html', {'reports': reports})


@login_required(login_url='user_login')
def vaccine_date_form(request):
    if not find_user(request)['d']:
        return render(request, 'not_auth.html', {})
    form = forms.VaccineDateForm(request.POST or None)
    if request.method == 'POST':
        form.save()
        date = request.POST.get('date')
        vaccine = request.POST.get('vaccine')
        message = f'{vaccine} vaccination will be on {date}'
        emails = [i.email for i in models.CustomerProfile.objects.all()]
        send_mail('Vaccine date announced', message,
                  'openoffice230@gmail.com', emails)
        messages.success(request, f'Vaccine date updated')
        return redirect(index)
    return render(request, 'form_template_v.html', {'form': form})


@login_required(login_url='user_login')
def visited_patients(request):
    if not (find_user(request)['d'] or find_user(request)['h']):
        return render(request, 'not_auth.html', {})

    appointments = []
    m = True
    if request.method == 'POST':
        try:
            start = request.POST.get('start')
            end = request.POST.get('end')
            # print(start, end)
            d = str(start).split('-')
            e = str(end).split('-')
            l = []
            for i in models.Appointment.objects.all():
                s = str(i.date).split('-')
                print(s)
                if int(d[2])<int(s[2])<int(e[2]):
                    l.append(i)
            appointments = l  
            if not appointments:
                messages.info(request, f'No data found')
        except:
            pass
    if (find_user(request)['d']):
        appointments = models.Appointment.objects.all().order_by('date')
        f = False
    else:
        f = True
    # appointments = models.Appointment.objects.all().order_by('date')
    # print(appointments)
    context = {'appointments': appointments, 'f':f}
    context.update(find_user(request))
    return render(request, 'visited_patients.html', context)

@login_required(login_url='user_login')
def lab_reports_hi(request):
    v = False
    if not (find_user(request)['d'] or find_user(request)['h']):
        return render(request, 'not_auth.html', {})
    appointments = []
    m = True
    if request.method == 'POST':
        v = True
        try:
            start = request.POST.get('start')
            end = request.POST.get('end')
            print('srtart:',start,'end:', end)
            # print(start, end)
            ddd = str(start).split('-')
            eee = str(end).split('-')
            d = int(ddd[2])
            e = int(eee[2])
            # print(int(ddd[2]), int(eee[2]))
            l = []
            ff = models.LabBooking.objects.all()
            # print('F = ', ff)
            for i in models.LabBooking.objects.all():
                # print('Date:',str(i.date))
                sss = str(i.date).split('-')[2].split()[0]
                # ddd = str(start).split('-')
                # eee = str(end).split('-')
                # print('s=',sss)
                # print(ddd, sss[2], eee)
                if int(d)<int(sss)<int(e):
                    l.append(i)
                    print('_______________________________')
            appointments = l  
            print(appointments)
            # if not appointments:
            #     messages.info(request, f'No data found')
        except:
            pass
    # appointments = models.Appointment.objects.all().order_by('date')
    # print(appointments)
    # appointments = models.LabBooking.objects.all()
    context = {'reports': appointments, 'v':v}
    context.update(find_user(request))
    return render(request, 'lab_reports_hi.html', context)


@login_required(login_url='user_login')
def prescriptions_to_lab(request):
    if not find_user(request)['d']:
        return render(request, 'not_auth.html', {})
    form = forms.PrescriptionsToLabForm(
        request.POST or None, request.FILES or None)
    if request.method == 'POST':
        instant = form.save(commit=False)
        instant.doctor_id = models.DoctorProfile.objects.get(
            user_id=request.user.id).id
        instant.save()
        messages.success(request, f'Prescriptions to lab success')
        return redirect(index)
    patients = models.CustomerProfile.objects.all()
    context = {'form': form, 'patients':patients}
    context.update(find_user(request))
    return render(request, 'form_template_p.html', context)

@login_required(login_url='user_login')
def view_prescriptions(request):
    prescriptions = models.PrescriptionsToLab.objects.filter(lab_id=models.Lab.objects.get(
            user_id=request.user.id).id)
    context = {'precs':prescriptions}
    context.update(find_user(request))
    return render(request,'lab_prescriptions.html', context)

def vacancy_apply(request):
    form = forms.VacancyApplyForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            instant = form.save(commit=False)
            instant.save()
            messages.success(request, f'Successfully applied')
            return redirect(index)
    jobs = models.Jobs.objects.filter(active=True)
    return render(request, 'form_template_vaccancy.html', {'form': form, 'jobs':jobs})


@login_required(login_url='user_login')
def recruit(request):
    if not find_user(request)['h']:
        return render(request, 'not_auth.html', {})
    applicants = models.VacancyApply.objects.all()
    return render(request, 'recruit.html', {'applicants': applicants})


@login_required(login_url='user_login')
def select(request, id):
    if not find_user(request)['h']:
        return render(request, 'not_auth.html', {})
    applicants = models.VacancyApply.objects.get(id=id)
    send_mail('Appointed', 'You have been appointed', 'questpython@gmail.com',
              [applicants.email, ], fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
    applicants.delete()
    return redirect(recruit)


def forgot_password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        user = User.objects.filter(username=username)
        if user:
            profile = models.CustomerProfile.objects.filter(user_id=user[0].id)
            if profile:
                p = profile[0]
                print(1)
                if p.mobile == mobile:
                    u = User.objects.get(username=username)
                    print(u.password)
                    u = authenticate(username=username)
                    if u is not None:
                        login(request, u)
                        return redirect('change_password')
                return render(request, 'message.html', {'message': 'Invalid mobile', 'no_record_check': 0})
            return render(request, 'message.html', {'message': 'Not a customer'})
        return render(request, 'message.html', {'message': 'No matching accounts found'})
    return render(request, 'forgot_password.html', {})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'form_template.html', {
        'form': form
    })


@login_required(login_url='user_login')
def appointmentlist(request):
    if not find_user(request)['c']:
        return render(request, 'not_auth.html', {})
    appointments = models.Appointment.objects.filter(patient=models.CustomerProfile.objects.get(
        user_id=request.user.id))
    return render(request, 'viewappointments.html', {'all': appointments})


@login_required(login_url='user_login')
def deleteappointment(request, id):
    if not find_user(request)['c']:
        return render(request, 'not_auth.html', {})
    models.Appointment.objects.get(id=id).delete()
    return redirect('viewappointments')


@login_required(login_url='user_login')
def editappointment(request, id):
    if not find_user(request)['c']:
        return render(request, 'not_auth.html', {})
    obj = models.Appointment.objects.get(id=id)
    form = forms.AppointmentForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('viewappointments')
    return render(request, 'form_template.html', {'form': form})


@login_required(login_url='user_login')
def lablist(request):
    if find_user(request)['c'] or find_user(request)['l'] or find_user(request)['d']:
        try:
            all = models.LabBooking.objects.filter(patient=models.CustomerProfile.objects.get(
            user_id=request.user.id))
        except:
            all = models.LabBooking.objects.filter(lab=models.Lab.objects.get(
            user_id=request.user.id))
    else:
        return render(request, 'not_auth.html', {})
    return render(request, 'viewalabs.html', {'all': all, 'c':find_user(request)['c']})

@login_required(login_url='user_login')
def reviewlist(request):
    if not find_user(request)['h']:
        return render(request, 'not_auth.html', {})
    if request.method == 'POST':
        id = request.POST['id']
        email = request.POST['email']
        reply = request.POST['reply']
        send_mail('Reply for review', reply,
                  'openoffice230@gmail.com', [email,])
        messages.success(request, f'Reply email sent')
        models.Review.objects.get(id=id).delete()
    reviews = models.Review.objects.all()
    return render(request, 'reviewslist.html', {'reviews': reviews})


@login_required(login_url='user_login')
def deletelabs(request, id):
    if not find_user(request)['c']:
        return render(request, 'not_auth.html', {})
    models.LabBooking.objects.get(id=id).delete()
    return redirect('lablist')


@login_required(login_url='user_login')
def editlabs(request, id):
    if not find_user(request)['c']:
        return render(request, 'not_auth.html', {})
    obj = models.LabBooking.objects.get(id=id)
    form = forms.LabBookingForm(request.POST or None, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('lablist')
    return render(request, 'form_template.html', {'form': form})


@login_required(login_url='user_login')
def review(request):
    if not find_user(request)['c']:
        return render(request, 'not_auth.html', {})
    form = forms.ReviewForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = models.CustomerProfile.objects.get(user_id=request.user.id)
            instance.save()
            messages.success(request, 'Your comment sent')
            return redirect('index')
    return render(request, 'form_template_review.html', {'form': form})

@login_required(login_url='user_login')
def updatevaccancy(request):
    if not find_user(request)['h']:
        return render(request, 'not_auth.html', {})
    if request.method == 'POST':
        msg = f"Total vaccany is {request.POST['count']}"                                                                                           
        send_mail('Total vaccanciew', msg,
                  'openoffice230@gmail.com', ['healthoffice463@gmail.com',])
        messages.success(request, f'Email sent')

    return render(request, 'updatevaccancy.html')

@login_required(login_url='user_login')
def vaccancylimit(request):
    form = forms.VaccancyLimitForm(request.POSt or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Success')
            return redirect('index')
    return render(request, 'form_template.html', {'form': form})