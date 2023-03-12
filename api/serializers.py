from rest_framework import serializers
from app.models import Department,Employees,Position

class DepartmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Department
		fields ='__all__'
		# fields =['id', 'category_name']
	
class EmployeesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Employees
		fields ='__all__'
		# fields =['id','item_title','item_text','item_image','item_category']

class PositionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Position
		fields ='__all__'