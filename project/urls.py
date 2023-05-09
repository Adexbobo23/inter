"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.view_login, name='login'),
    path('register/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('account_statement/', views.account_statement, name='account_statement'),
    path('add_beneficiary/', views.add_beneficiary, name='add_beneficiary'),
    path('Add_Remittance_Request/', views.Add_Remittance_Request, name='Add_Remittance_Request'),
    path('Apply_for_Loan/', views.Apply_for_Loan, name='Apply_for_Loan'),
    path('beneficiary_list/', views.beneficiary_list, name='beneficiary_list'),
    path('change_password/', views.change_password, name='change_password'),
    path('FD_List/', views.FD_List, name='FD_List'),
    path('FD_schemes/', views.FD_schemes, name='FD_schemes'),
    path('generate_ticket/', views.generate_ticket, name='generate_ticket'),
    path('loan_status/', views.loan_status, name='loan_status'),
    path('open_fd/', views.open_fd, name='open_fd'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('results/', views.results, name='results'),
    path('ticket_list/', views.ticket_list, name='ticket_list'),
    path('Transfer_Fund/', views.Transfer_Fund, name='Transfer_Fund'),
    path('Withdraw_FD/', views.Withdraw_FD, name='Withdraw_FD'),
]
