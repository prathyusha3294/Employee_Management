from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import status, mixins, generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny,IsAuthenticatedOrReadOnly
from .serializers import EmployeeSerializer
# from django.http import JsonResponse
# from .forms import EmployeeForm

def getEmployeeList(request):
    # Render the employee list page
    return render(request, 'employee/employee_list.html')

class EmployeeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    """Manage Attachment in the Database"""

    permission_classes = (AllowAny, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer