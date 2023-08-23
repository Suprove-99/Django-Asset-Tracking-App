from rest_framework import generics
from .models import Company, Employee, Device, DeviceAssignment
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceAssignmentSerializer


class CompanyListCreateView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    # def get_queryset(self):
    #     user = self.request.user
    #     return Company.objects.filter(user=user)


class CompanyDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    #
    # def get_queryset(self):
    #     user = self.request.user
    #     return Company.objects.filter(user=user)


class EmployeeListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(company__user=user)


class EmployeeDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        user = self.request.user
        return Employee.objects.filter(company__user=user)

class DeviceListCreateView(generics.ListCreateAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        user = self.request.user
        return Device.objects.filter(company__user=user)

class DeviceDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        user = self.request.user
        return Device.objects.filter(company__user=user)

class DeviceAssignmentListCreateView(generics.ListCreateAPIView):
    serializer_class = DeviceAssignmentSerializer

    def get_queryset(self):
        user = self.request.user
        return DeviceAssignment.objects.filter(employee__company__user=user)

class DeviceAssignmentDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceAssignmentSerializer

    def get_queryset(self):
        user = self.request.user
        return DeviceAssignment.objects.filter(employee__company__user=user)
