from django.urls import path
from .views import (
    CompanyListCreateView, CompanyDetailUpdateDeleteView, EmployeeListCreateView, EmployeeDetailUpdateDeleteView,
    DeviceListCreateView, DeviceDetailUpdateDeleteView, DeviceAssignmentListCreateView,
    DeviceAssignmentDetailUpdateDeleteView,
)

urlpatterns = [

    path('api/companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('api/companies/<int:pk>/', CompanyDetailUpdateDeleteView.as_view(), name='company-detail-update-delete'),

    path('api/employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('api/employees/<int:pk>/', EmployeeDetailUpdateDeleteView.as_view(), name='employee-detail-update-delete'),

    path('api/devices/', DeviceListCreateView.as_view(), name='device-list-create'),
    path('api/devices/<int:pk>/', DeviceDetailUpdateDeleteView.as_view(), name='device-detail-update-delete'),

    path('api/assignments/', DeviceAssignmentListCreateView.as_view(), name='deviceassignment-list-create'),
    path('api/assignments/<int:pk>/', DeviceAssignmentDetailUpdateDeleteView.as_view(),
         name='deviceassignment-detail-update-delete'),
]


