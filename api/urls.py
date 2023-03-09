from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views
from .views import *


urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
 
	path('departments-list/', views.departmentsList, name="department-list"),
	path('department-detail/<str:pk>/', views.departmentsDetail, name="department-detail"),
	path('department-create/', views.departmentsCreate, name="department-create"),
	path('department-delete/<str:pk>/', views.departmentsDelete, name="department-delete"),
	path('department-update/<str:pk>/', views.departmentsUpdate, name="department-update"),
 
 
	path('positions-list/', views.positionsList, name="positions-list"),
	path('position-detail/<str:pk>/', views.positionDetail, name="position-detail"),
	path('position-create/', views.positionCreate, name="position-create"),
	path('position-delete/<str:pk>/', views.positionDelete, name="position-delete"),
	path('position-update/<str:pk>/', views.positionUpdate, name="position-update"),
  
	path('employees-list/', views.employeesList, name="employees-list"),
	path('employee-detail/<str:pk>/', views.employeesDetail, name="employee-detail"),
	path('employee-create/', views.employeeCreate, name="employee-create"),
	path('employee-delete/<str:pk>/', views.employeeDelete, name="employee-delete"),
	path('employee-update/<str:pk>/', views.employeeUpdate, name="employee-update"),
 
 ]
