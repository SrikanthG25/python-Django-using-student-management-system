from django.shortcuts import render
from rest_framework import generics ,permissions
from .models import StudentModel , LoginUser
from .serializers import StudentSerializer , LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .Authentications import create_access_token ,decode_acsess_token 


class StudentRegister(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []
    def post(self, request):
        data = request.data
        student = StudentSerializer(data=request.data)
        login = LoginSerializer(data=request.data)
        try:         
            if student.is_valid():
                student.save()
            if login.is_valid():
                login.save(UserName=data.get('UserName'), Password = data.get('Password'))
            return Response(student.data, status=status.HTTP_201_CREATED)
        
        except StudentModel.DoesNotExist:
            return Response({'message' : 'To give valid Data '}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self , request , pk=None):
        try:
            if pk is not None:
                student = StudentModel.objects.filter(pk=pk)
                serializer = StudentSerializer(student , many = True)
                return Response(serializer.data)
            else:
                student = StudentModel.objects.all()
                serializer = StudentSerializer(student , many = True)
                return Response(serializer.data)
        except Exception:
            return Response({'message' : 'Student Not found '} , status=status.HTTP_404_NOT_FOUND)

    def put(self,request ,pk=None):
        try:
            if pk is not None:
                student = StudentModel.objects.get(id=pk)
                Stu_serializer = StudentSerializer(student , data=request.data)
                if Stu_serializer.is_valid():
                    Stu_serializer.save()
                    return Response(Stu_serializer.data)
        except Exception:
            return Response({'error': 'Please provide a valid ID '}, status=status.HTTP_400_BAD_REQUEST)
       
class LoginView(generics.GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = []
    def post(self,request):
        try:
            UserName = request.data['UserName']
            Password = request.data['Password']

            user = LoginUser.objects.filter(UserName=UserName).first()

            if Password == user.Password:
                access_token = create_access_token(user.id)
                data = {
                    'token' : access_token ,
                    'message' : 'Token Successfully Generated'
                }
            return Response(data )
        except Exception:
            return Response({'message' : 'User Not Found , TO given an Valid UserName and Password'} , status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        try:
            user = get_authorization_header(request).split()

            if user and len(user) == 2:
                token = user[1].decode('utf-8')
                id = decode_acsess_token(token)
                user = StudentModel.objects.filter(pk=id).first()
                return Response(StudentSerializer(user).data) 
            raise AuthenticationFailed('UnAuthorized to retry')
        except StudentModel.DoesNotExist:
            raise AuthenticationFailed('User not found')

        