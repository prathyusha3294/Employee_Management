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
# # Get list of all employees
# def fetchEmployeeList(request):
#     try:
#         employees = Employee.objects.all()
#         employeeData = [
#             {
#                 'id': employee.id,
#                 'name': employee.name,  # Use 'name' directly from the model
#                 'email': employee.email,  # Use 'email' directly from the model
#                 'age': employee.age,  # Use 'age' directly from the model
#                 'gender': employee.gender,  # Use 'gender' directly from the model
#                 'phoneNo': employee.phoneNo,  # Include other fields if needed
#                 'addressDetails': employee.addressDetails,
#                 'workExperience': employee.workExperience,
#                 'qualifications': employee.qualifications,
#                 'projects': employee.projects,
#                 'photo': employee.photo,
#             } for employee in employees
#         ]
#         return JsonResponse({'employees': employeeData}, status=200)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)


# # Create a new employee
# @csrf_exempt


# def createEmployee(request):
#     if request.method == 'POST':
#         try:
#             # Parse JSON data from the request body
#             data = json.loads(request.body)

#             # Initialize the form with the parsed data
#             form = EmployeeForm(data)
#             if form.is_valid():
#                 form.save()
#                 return JsonResponse({'message': 'Employee created successfully!'}, status=201)
#             else:
#                 return JsonResponse({'errors': form.errors}, status=400)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON format'}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)
#     return JsonResponse({'error': 'Invalid request method'}, status=400)


# # Update an existing employee
# @csrf_exempt
# def updateEmployee(request, employeeId):
#     try:
#         employee = get_object_or_404(Employee, pk=employeeId)
#         if request.method == 'POST':
#             form = EmployeeForm(request.POST, instance=employee)
#             if form.is_valid():
#                 form.save()
#                 return JsonResponse({'message': 'Employee updated successfully!'}, status=200)
#             else:
#                 return JsonResponse({'errors': form.errors}, status=400)
#         return JsonResponse({'error': 'Invalid request method'}, status=400)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)

# # Delete an employee
# @csrf_exempt
# def deleteEmployee(request, employeeId):
#     try:
#         employee = get_object_or_404(Employee, pk=employeeId)
#         if request.method == 'DELETE':
#             employee.delete()
#             return JsonResponse({'message': 'Employee deleted successfully!'}, status=200)
#         return JsonResponse({'error': 'Invalid request method'}, status=400)
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)


class EmployeeViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,mixins.RetrieveModelMixin):
    """Manage Attachment in the Database"""

    permission_classes = (AllowAny, )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer