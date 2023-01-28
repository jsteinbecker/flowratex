from django.contrib import admin
from .models import (
    JobGroup, Team, Shift, Employee, Schedule, Period, Week, Workday,
    Slot
)

# Register your models here.
@admin.register(JobGroup)
class JobGroupAdmin (admin.ModelAdmin):
    list_display = ('name', 'team')
    list_filter = ('team',)
    search_fields = ('name',)
    
@admin.register(Team)
class TeamAdmin (admin.ModelAdmin):
    list_display = ('name', 'initial_date', 'n_periods')
    search_fields = ('name',)
    
@admin.register(Shift)
class ShiftAdmin (admin.ModelAdmin):
    list_display = ('name', 'start_time', 'group', 'weekdays')
    list_filter = ('group',)
    search_fields = ('name',)
    
@admin.register(Employee)
class EmployeeAdmin (admin.ModelAdmin):
    list_display = ('name', 'team', 'date_of_hire', 'active')
    fieldsets = (
        ('Employee', {
            'fields': ('name', 'team', 'date_of_hire', 'active')
        }),
        ('FTE', {
            'fields': ('fte',)
        }),
        ('Shifts', {
            'fields': ('shifts_trained', 'shifts_available')
        }),
    )
    list_filter = ('team', 'active')
    search_fields = ('name',)
    
admin.register(Schedule)
admin.register(Period)
admin.register(Week)
admin.register(Workday)
admin.register(Slot)



