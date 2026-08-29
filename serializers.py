from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    salary = serializers.IntegerField()
    email = serializers.EmailField()
    address = serializers.CharField()
    role = serializers.CharField()

    def validate_salary(self,salary):
        if salary<0:
            raise serializers.ValidationError("Salary cannot be negative")

        return salary

    def validate_email(self,email):
        normalized_email = email.strip().lower()

        if Employee.objects.filter(email__iexact = normalized_email).exists():
            raise serializers.ValidationError("Employee with the given email exists")

        domain = normalized_email.rsplit('@',1)[-1]

        if domain != 'gmail.com':
            raise serializers.ValidationError('only gmail ccount are allowed')

        return normalized_email

    def create(self,validated_data):
        emp = Employee.objects.create(**self.validated_data)
        return emp

        
    def update(sef,instance,validate_data):
        instance.name=validate_data.get('name',instance.name)
        instance.salary=validate_data.get('salary',instance.salary)
        instance.email=validate_data.get('email',instance.email)
        instance.address=validate_data.get('address',instance.address)
        instance.role=validate_data.get('role',instance.role)
        instance.save()

        return instance