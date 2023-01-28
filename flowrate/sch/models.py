from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class JobGroup (models.Model):
    name = models.CharField(max_length=10)
    team = models.ForeignKey("Team", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
  
    
class Team (models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    initial_date = models.DateField()
    n_periods = models.IntegerField(default=3)
    
    def __str__(self):
        return self.name


DAYCHOICES=(
        (0,"Sunday"),(1,"Monday"),(2,"Tuesday"),(3,"Wednesday"),(4,"Thursday"),(5,"Friday"),(6,"Saturday")
) 
class Shift (models.Model):
    name = models.CharField (max_length=10)
    start_time = models.TimeField()
    group = models.ForeignKey (JobGroup, on_delete=models.CASCADE)
    weekdays = MultiSelectField (choices=DAYCHOICES, max_choices=7,max_length=14,default=[0,1,2,3,4,5,6])
    
    def __str__(self):
        return self.name
   
    
class Employee (models.Model):
    name = models.CharField(max_length=10)
    fte = models.FloatField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    shifts_trained = models.ManyToManyField(Shift, related_name="shifts_trained")
    shifts_available = models.ManyToManyField(Shift, related_name="shifts_available")
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    date_of_hire = models.DateField()
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
 
    
class Schedule (models.Model):
    start_date = models.DateField()
    team  = models.ForeignKey(Team, on_delete=models.CASCADE)
    employees  = models.ManyToManyField(Employee)
    periods = models.ForeignKey("Period", on_delete=models.CASCADE, related_name="periods", auto_created=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Period (models.Model):
    number = models.IntegerField()
    start_date = models.DateField()
    weeks = models.ForeignKey("Week", on_delete=models.CASCADE)
  
    
class Week (models.Model):
    number = models.IntegerField()
    days = models.ForeignKey("Workday", on_delete=models.CASCADE)
    
            
class Workday (models.Model):
    date = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.date.strftime("%a %b %d, %Y")


class Slot (models.Model):
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    workday = models.ForeignKey(Workday, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.shift.name