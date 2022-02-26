from django.shortcuts import render
from .models import Patient
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        fname = request.POST.get('f_name')
        lname = request.POST.get('l_name')
        gender = request.POST.get('gender')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        visitDate = request.POST.get('visitDate')

        if mobile.isdigit():
            data = Patient(f_name=fname, l_name=lname, gender=gender, mobile=mobile, email=email
                           , address=address, visitDate=visitDate)
            data.save()
            messages.success(request, "Appointment Sucssefully")

        else:
            messages.error(request, "Re-enter mobile number")

    return render(request, 'home.html')
