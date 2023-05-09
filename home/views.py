from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'index.html')

def view_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Password not match")

        else:
            myuser = User.objects.create_user(uname, email, pass1)
            myuser.save()
            return redirect('login')
    return render(request, 'signup.html')
    
@login_required
def dashboard(request):
    return render (request, 'dashboard.html')
@login_required
def account_statement(request):
    return render(request, 'account_statement.html')
@login_required
def add_beneficiary(request):
    return render(request, 'add_beneficiary.html')
@login_required
def Add_Remittance_Request(request):
    return render(request, 'Add_Remittance_Request.html')
@login_required
def Apply_for_Loan(request):
    return render(request, 'Apply_for_Loan.html')
@login_required
def beneficiary_list(request):
    return render(request, 'beneficiary_list.html')
@login_required
def change_password(request):
    return render(request, 'change_password.html')
@login_required
def FD_List(request):
    return render(request, 'FD_List.html')
@login_required
def FD_schemes(request):
    return render(request, 'FD_schemes.html')
@login_required
def generate_ticket(request):
    return render(request, 'generate_ticket.html')
@login_required
def loan_status(request):
    return render(request, 'loan_status.html')
@login_required
def open_fd(request):
    return render(request, 'open_fd.html')
@login_required
def profile_page(request):
    return render(request, 'profile_page.html')
@login_required
def results(request):
    return render(request, 'results.html')
@login_required
def ticket_list(request):
    return render(request, 'ticket_list.html')
@login_required
def Transfer_Fund(request):
    return render(request, 'Transfer_Fund.html')
@login_required
def Withdraw_FD(request):
    return render(request, 'Withdraw_FD.html')

