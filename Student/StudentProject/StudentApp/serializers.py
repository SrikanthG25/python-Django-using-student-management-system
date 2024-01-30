from rest_framework import serializers
from .models import StudentModel , LoginUser

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields =  '__all__'



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoginUser
        fields =  '__all__'
