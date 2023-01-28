from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, DeleteView, ListView, DetailView

from .models import (
    JobGroup, Team, Shift, Employee, Schedule, Period, Week, Workday,
    Slot
)

# Create your views here.
class EmployeeList (ListView):
    model               = Employee
    template_name       = 'sch/employee-list.pug'
    context_object_name = 'employees'
    queryset            = Employee.objects.all()
    paginate_by         = 3
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = Team.objects.get(name='NCMC')
        return context
    
class EmployeeDetail (DetailView):
    model               = Employee
    template_name       = 'sch/employee-detail.pug'
    context_object_name = 'employee'
    queryset            = Employee.objects.all()
    
    