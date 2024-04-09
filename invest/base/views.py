from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from . forms import CustomerProfileForm, CustomerRegistrationForm
from django.views import *
from . models import Product, Customer
from . forms import CustomerProfileForm, CustomerRegistrationForm, UserProfileForm
from django.contrib import messages


# Create your views here.

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
        # totalitem = 0
        # wishitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user=request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
        return render(request, 'profile.html', locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']
            country = form.cleaned_data['country']

            reg = Customer(user=user, name=name, mobile=mobile, zipcode=zipcode, country=country)
            reg.save()
            messages.success(request, "Congratulations! Profile Saved Successfully")
        else:
            messages.warning(request, "Invalid Input Data")
        return render(request, 'profile.html', locals())


# @login_required     
def address(request):
    add = Customer.objects.filter(user=request.user)
    # totalitem = 0
    # wishitem = 0
    # if request.user.is_authenticated:
    #     totalitem = len(Cart.objects.filter(user=request.user))
    #     wishitem = len(Wishlist.objects.filter(user=request.user))
    return render(request, 'address.html', locals())


class updateAddress(View):
    def get(self,request,pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        # totalitem = 0
        # wishitem = 0
        # if request.user.is_authenticated:
        #     totalitem = len(Cart.objects.filter(user=request.user))
        #     wishitem = len(Wishlist.objects.filter(user=request.user))
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