from django.shortcuts import render, redirect
from ..models import *
from django.contrib.auth.hashers import make_password
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
        
    def post(self, request):
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        password = request.POST.get("password")
        values = {
            'firstname': firstname,
            'lastname': lastname,
            'mobile': mobile,
            'email': email
        }
        customer = Customer(firstname=firstname, lastname=lastname,
                            mobile=mobile, email=email, password=password)
        error_msg = self.validateCustomer(customer)

        if not error_msg:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('homepage')
        else:
            data = {
                "error": error_msg,
                "value": values
            }
            return render(request, 'signup.html', data)


    def validateCustomer(self, customer):
        error_msg = None
        if not customer.firstname:
            error_msg = "First name required !!!"
        elif len(customer.firstname) < 4:
            error_msg = "First name must be 4 char long !!!"
        elif not customer.lastname:
            error_msg = "Last name required !!!"
        elif len(customer.lastname) < 4:
            error_msg = "Last name must be 4 char long !!!"
        elif not customer.mobile:
            error_msg = "Mobile Number required !!!"
        elif len(customer.mobile) < 10 or len(customer.mobile) > 10:
            error_msg = "Mobile Number must be of 10 digits !!!"
        elif not customer.password:
            error_msg = "Password required !!!"
        elif len(customer.lastname) < 5:
            error_msg = "Password must be 5 char long !!!"
        elif customer.isExists():
            error_msg = "Email already registred !!!"
        return error_msg

