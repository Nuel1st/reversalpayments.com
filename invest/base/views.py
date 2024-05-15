from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from . forms import CustomerProfileForm, CustomerRegistrationForm
from django.views import *
from . models import Product, Customer
from . forms import CustomerProfileForm, CustomerRegistrationForm, UserProfileForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import DepositForm
from .models import Deposit

# Create your views here.

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            # last activity time from the session
            last_activity = request.session.get('last_activity')
            if last_activity:
                # Calculating the time difference
                inactive_time = timezone.now() - last_activity
                # Define inactive threshold
                inactive_threshold = timezone.timedelta(minutes=10)
                # Log out the user if inactive for longer than the threshold
                if inactive_time > inactive_threshold:
                    logout(request)
            # Update the last activity time in the session
            request.session['last_activity'] = timezone.now()
        return response

def home(request):
    # orders
    return render( request, 'index.html', locals())

def registerPage(request):
    form = UserCreationForm() 

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, register.html, context)

def loginPage(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'detail.html')

def service(request):
    return render(request, 'service.html')

def plan(request):
    return render(request, 'plan.html')

def faq(request):
    return render(request, 'faq.html')

def signal(request):
    return render(request, 'signal.html')


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'customerregistration.html', locals())
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations! User Registration Successful")
        else:
            messages.error(request, "Invalid Input Data")
        return render(request, 'customerregistration.html', locals())

class RegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'main_registration.html', locals())

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request, 'profile.html', locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']
            country = form.cleaned_data['country']
            Area = form.cleaned_data['area']

            reg = Customer(user=user, name=name, mobile=mobile, zipcode=zipcode, country=country)
            reg.save()
            messages.success(request, "Congratulations! Profile Saved Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'index.html', locals())


# @login_required     
def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request, 'address.html', locals())


class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(request, 'updateAddress.html', locals())
    def post(self,request,pk):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.mobile = form.cleaned_data['mobile']
            add.zipcode = form.cleaned_data['zipcode']
            add.country = form.cleaned_data['country']
            add.save()
            messages.success(request, "Congratulations! Profile Updated Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return redirect("address")
       
def edit_profile(request):
    if request.method =='POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def deposit_funds(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            deposit.save()
            messages.success(request, 'Deposit successful!')
            return redirect('dashboard')  # Redirect to the user's dashboard
    else:
        form = DepositForm()
    return render(request, 'deposit_funds.html', {'form': form})

@login_required
def dashboard(request):
    deposits = Deposit.objects.filter(user=request.user)
    total_deposit = sum(deposit.amount for deposit in deposits)
    return render(request, 'dashboard.html', {'deposits': deposits, 'total_deposit': total_deposit})