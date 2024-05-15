from django.urls import path
from . import views 
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm, MyPasswordChangeForm, MySetPasswordForm


urlpatterns= [
    path('',  views.home, name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('about/', views.about, name="about" ),
    path('contact/', views.contact, name="contact"),
    path('plan/', views.plan, name="plan"),
    path('service/', views.service, name="service"),
    path('faq/', views.faq, name="faq"),
    path('signal/', views.signal, name="signal"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('deposit/', deposit_funds, name='deposit_funds'),
    path('dashboard/', dashboard, name='dashboard'),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
    # path('project/', views.project, name="project")


    path('main-registration/', views.RegistrationView.as_view(), name="main_registration" ),

    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm) , name='login'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='changepassword.html', success_url='/passwordchangedone'), name='passwordchange'),
    # path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='changepassword.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone'), name='passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),

    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    # path('password-reset/', auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done', auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    

    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "ReversalPayments"
admin.site.site_title = "ReversalPayments"
admin.site.site_index_title = " Welcome to ReversalPayments"