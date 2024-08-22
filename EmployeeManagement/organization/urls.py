from django.urls import path,include
from . import views
from rest_framework import routers
from organization.views import *

app_name = "organization"

company_router = routers.SimpleRouter()
company_router.register('master/employee', EmployeeViewSet, basename='company')

urlpatterns = [
    path('', views.getEmployeeList, name='getEmployeeList'), 
    path('',include(company_router.urls)),
    # path('employees/', views.fetchEmployeeList, name='fetchEmployeeList'),  # API to get employee data
    # path('create/', views.createEmployee, name='createEmployee'),
    # path('<int:employeeId>/edit/', views.updateEmployee, name='updateEmployee'),
    # path('<int:employeeId>/delete/', views.deleteEmployee, name='deleteEmployee'),
]


