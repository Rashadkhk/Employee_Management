from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.utils import translation  # Import translation module
from .serializers import RegisterSerializer, UserSerializer, DepartmentSerializer, PositionSerializer, EmployeeSerializer
from .models import Department, Position, Employee
from .permissions import IsStaffOrReadOnly 

# Register
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

# Employee
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        language_code = request.GET.get('lang', 'en')[:2]
        translation.activate(language_code)
        return super().get(request, *args, **kwargs)

class DepartmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

    def get(self, request, *args, **kwargs):
        language_code = request.GET.get('lang', 'en')[:2]
        translation.activate(language_code)
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        language_code = request.GET.get('lang', 'en')[:2]
        translation.activate(language_code)
        return super().delete(request, *args, **kwargs)

# Current user Profile
class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

# Dept
class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        language_code = request.GET.get('lang', 'en')[:2]  
        translation.activate(language_code)
        print(f'Activated Language: {translation.get_language()}')
        return super().get(request, *args, **kwargs)

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

    def get(self, request, *args, **kwargs):
        language_code = request.GET.get('lang', 'en')[:2]
        translation.activate(language_code)
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        language_code = request.GET.get('lang', 'en')[:2]
        translation.activate(language_code)
        return super().delete(request, *args, **kwargs)
    

# Position
class PositionListCreateView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request': self.request}

    def get(self, request, *args, **kwargs):
        language_code = request.GET.get('lang', 'en')[:2]
        translation.activate(language_code)
        return super().get(request, *args, **kwargs)

class PositionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAuthenticated, IsStaffOrReadOnly]

    def get(self, request, *args, **kwargs):
        language_code = request.GET.get('lang', 'en')[:2]
        translation.activate(language_code)
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        language_code = request.GET.get('lang', 'en')[:2]
        translation.activate(language_code)
        return super().delete(request, *args, **kwargs)


