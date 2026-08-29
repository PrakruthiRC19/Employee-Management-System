from django.http import JsonResponse
from .models import Employee
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .serializers import EmployeeSerializer


def build_response(message, status, data=None, errors=None):
    response_data = {
        "message": message
    }

    if data:
        response_data["data"] = data

    if errors:
        response_data["errors"] = errors

    return JsonResponse(response_data, status=status)


@csrf_exempt
@api_view(["GET","POST"])
def employee_list_view(request):

    if request.method == "GET":

        employees = Employee.objects.all()

        serializer = EmployeeSerializer(employees,many=True)

        return build_response('Employee retrived successfully', status=200, data=serializer.data)

    if request.method == "POST":

        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return build_response(
                "Employee created successfully",
                status=201,
                data=serializer.data
            )

        return build_response(
            "Validation Failed",
            status=400,
            errors=serializer.errors
        )


@csrf_exempt
@api_view(['GET','PUT','PATCH','DELETE'])
def employee_details_view(request, employee_id):

    try:
        employee = Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        return build_response("employee id not exists",status=404)

    if request.method == "GET":

        serializer = EmployeeSerializer(instance=employee)

        return build_response(
            "Employee found successfully",
            status=200,
            data=serializer.data
        )

    if request.method == "PUT":

        request_data = json.loads(request.body)

        field_list = ["name", "salary", "email", "address", "role"]
        missing_fields = []

        for field in field_list:
            if field not in request_data:
                missing_fields.append(field)

        if missing_fields:

            errors = {
                'missing fields':missing_fields
            }

            return build_response(
                "Mandatory fields are missing", 
                status=400, 
                errors=errors
            )

        serializer = EmployeeSerializer(data=request_data,instance=employee)

        if serializer.is_valid():
            serializer.save()

            return build_response(
                "Employee updated successfully",
                status=200,
                data=serializer.data
            )

        return build_response(
            "Validation Failed",
            status=400,
            errors=serializer.errors
        )

    if request.method == 'PATCH':
        serializer = EmployeeSerializer(data=request.data,instance=employee,partial=True)

        if serializer.is_valid():
            serializer.save()

            return build_response(
                "Employee modified successfully",
                status=200,
                data=serializer.data
            )
            
        return build_response(
            "Validation Failed",
            status=400,
            errors=serializer.errors
        )

    if request.method == "DELETE":

        serializer = EmployeeSerializer(instance=employee)

        employee.delete()

        return build_response(
            "Employee deleted successfully",
            status=200,
            data=serializer.data
        )

# @csrf_exempt
# @api_view(['GET','POST'])
# def employee_list_view(request):
#     if request.method=='GET':
#         employee = Employee.objects.all()
#     return JsonResponse(
#         {
#             "message":"Dummy APi executed uccessfully"
#         }
#     )