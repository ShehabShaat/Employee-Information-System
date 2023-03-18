from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from app.views import *

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
	"departments-list":'departments-list/',
	"department-create":'department-create/',
	"department-detail":'department-detail/<str:pk>/',
	"department-delete":'department-delete/<str:pk>/',
	"department-update":'department-update/<str:pk>/',
 
 "===========================================================":"",
 
 	"positions-list":'positions-list/',
	"position-create":'position-create/',
	"position-detail":'position-detail/<str:pk>/',
	"position-delete":'position-delete/<str:pk>/',
	"position-update":'position-update/<str:pk>/',
 
 "============================================================":"",
 	"employees-list":'employees-list/',
	"employee-create":'employee-create/',
	"employee-detail":'employee-detail/<str:pk>/',
	"employee-delete":'employee-delete/<str:pk>/',
	"employee-update":'employee-update/<str:pk>/'
 
		}

	return Response(api_urls)

@api_view(['GET'])
def departmentsList(request):
	departments = Department.objects.all().order_by('-id')
	serializer = DepartmentSerializer(departments, many=True) # many=True ممكن يكون اكثر من واحد
	return Response(serializer.data) # شكل الداتا النهائي
@login_required

@api_view(['GET'])
def departmentsDetail(request, pk):
	departments = Department.objects.get(id=pk)
	serializer = DepartmentSerializer(departments, many=False)
	return Response(serializer.data)

@login_required
@api_view(['POST'])
def departmentsCreate(request):
	serializer = DepartmentSerializer(data=request.data) # اعملي فورم للداتا عشان اعبيها

	if serializer.is_valid():
		serializer.save()
       
	return Response(serializer.data)
@login_required
@api_view(['POST'])
def departmentsUpdate(request, pk):
	categories = Department.objects.get(id=pk)
	serializer = DepartmentSerializer(instance=categories, data=request.data)

	if serializer.is_valid():
		serializer.save()
	

	return Response(serializer.data)



@api_view(['DELETE'])
def departmentsDelete(request, pk):
	departments = Department.objects.get(id=pk)
	departments.delete()

	return Response('Item succsesfully delete!')

# # ========================================================================================


@api_view(['GET'])
def positionsList(request):
	position = Position.objects.all().order_by('-id')
	serializer = PositionSerializer(position, many=True) # many=True ممكن يكون اكثر من واحد
	return Response(serializer.data) # شكل الداتا النهائي

@api_view(['GET'])
def positionDetail(request, pk):
	position = Position.objects.get(id=pk)
	serializer = PositionSerializer(position, many=False)
	return Response(serializer.data)

@login_required
@api_view(['POST'])
def positionCreate(request):
	serializer = PositionSerializer(data=request.data) # اعملي فورم للداتا عشان اعبيها

	if serializer.is_valid():
		serializer.save()
       

	return Response(serializer.data)

@login_required
@api_view(['POST'])
def positionUpdate(request, pk):
	position = Position.objects.get(id=pk)
	serializer = PositionSerializer(instance=position, data=request.data)

	if serializer.is_valid():
		serializer.save()
	

	return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def positionDelete(request, pk):
	position = Position.objects.get(id=pk)
	position.delete()

	return Response('Item succsesfully delete!')


#  ========================================================================================
@api_view(['GET'])
def employeesList(request):
	employees = Employees.objects.all().order_by('-id')
	serializer = EmployeesSerializer(employees, many=True) # many=True ممكن يكون اكثر من واحد
	return Response(serializer.data) # شكل الداتا النهائي

@api_view(['GET'])
def employeesDetail(request, pk):
	employees = Employees.objects.get(id=pk)
	serializer = EmployeesSerializer(employees, many=False)
	return Response(serializer.data)

@login_required
@api_view(['POST'])
def employeeCreate(request):
	serializer = EmployeesSerializer(data=request.data) # اعملي فورم للداتا عشان اعبيها

	if serializer.is_valid():
		serializer.save()
       

	return Response(serializer.data)

@login_required
@api_view(['POST'])
def employeeUpdate(request, pk):
	employees = Employees.objects.get(id=pk)
	serializer = EmployeesSerializer(instance=employees, data=request.data)

	if serializer.is_valid():
		serializer.save()
	

	return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def employeeDelete(request, pk):
	employees = Employees.objects.get(id=pk)
	employees.delete()
	return Response('Item succsesfully delete!')