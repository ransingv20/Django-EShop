from django.shortcuts import render, redirect, HttpResponseRedirect
from store.models import *
from django.contrib.auth.hashers import  check_password
from django.views import View


class Login(View):
    return_url = None
    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        obj = Customer.get_custmer_by_email(email)
        print(obj)
        error_msg = None
        if obj:
            flag = check_password(password, obj.password)
            if flag:
                request.session['customer'] = obj.id
                # request.session['customer_email'] = obj.email
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url =  None
                    return redirect('homepage')
            else:
                error_msg = "Invalid Email or Password !!"
        else:
            error_msg = "Invalid Email or Password !!"

        return render(request, 'login.html', {"error": error_msg})
    
def logout(request):
    request.session.clear() 
    return redirect('login')   