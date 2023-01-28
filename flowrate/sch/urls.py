from django.urls import path, include
from .views import EmployeeList, EmployeeDetail


urlpatterns = [
    path('employee/', EmployeeList.as_view(), name='emplList'),
    path('employee/<int:pk>/', EmployeeDetail.as_view(), name='emplDetail'),
]
