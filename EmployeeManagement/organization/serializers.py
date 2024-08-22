from rest_framework import serializers
from .models import Employee

# Nested Serializer for Address Details
class AddressDetailsSerializer(serializers.Serializer):
    hno = serializers.CharField(max_length=255, required=False)
    street = serializers.CharField(max_length=255, required=False)
    city = serializers.CharField(max_length=255, required=False)
    state = serializers.CharField(max_length=255, required=False)

# Nested Serializer for Work Experience
class WorkExperienceSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=255, required=False)
    from_date = serializers.CharField(max_length=20, required=False)
    to_date = serializers.CharField(max_length=20, required=False)
    address = serializers.CharField(max_length=255, required=False)

# Nested Serializer for Qualifications
class QualificationSerializer(serializers.Serializer):
    qualification_name = serializers.CharField(max_length=255, required=False)
    percentage = serializers.FloatField(required=False)

# Nested Serializer for Projects
class ProjectSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(max_length=500, required=False)
    photo = serializers.CharField(max_length=1000, required=False)  # Adjust length as needed for base64

# Main Serializer for Employee
class EmployeeSerializer(serializers.ModelSerializer):
    addressDetails = AddressDetailsSerializer(required=False)
    workExperience = WorkExperienceSerializer(many=True, required=False)
    qualifications = QualificationSerializer(many=True, required=False)
    projects = ProjectSerializer(many=True, required=False)

    class Meta:
        model = Employee
        fields = [
            'id', 'name', 'email', 'age', 'gender', 'phoneNo',
            'addressDetails', 'workExperience', 'qualifications',
            'projects'
        ]

    def create(self, validated_data):
        # Extract nested data
        address_details_data = validated_data.pop('addressDetails', None)
        work_experience_data = validated_data.pop('workExperience', [])
        qualifications_data = validated_data.pop('qualifications', [])
        projects_data = validated_data.pop('projects', [])

        # Create the employee instance
        employee = Employee.objects.create(**validated_data)

        # Handle nested data
        if address_details_data:
            employee.addressDetails = address_details_data
        
        if work_experience_data:
            employee.workExperience = work_experience_data
        
        if qualifications_data:
            employee.qualifications = qualifications_data
        
        if projects_data:
            employee.projects = projects_data

        employee.save()
        return employee

    def update(self, instance, validated_data):
        # Extract nested data
        address_details_data = validated_data.pop('addressDetails', None)
        work_experience_data = validated_data.pop('workExperience', [])
        qualifications_data = validated_data.pop('qualifications', [])
        projects_data = validated_data.pop('projects', [])

        # Update the employee instance
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phoneNo = validated_data.get('phoneNo', instance.phoneNo)

        # Handle nested data
        if address_details_data:
            instance.addressDetails = address_details_data
        
        if work_experience_data:
            instance.workExperience = work_experience_data
        
        if qualifications_data:
            instance.qualifications = qualifications_data
        
        if projects_data:
            instance.projects = projects_data

        instance.save()
        return instance
