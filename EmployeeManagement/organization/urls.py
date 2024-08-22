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
]


