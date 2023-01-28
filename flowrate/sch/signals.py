from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Schedule, Slot, Period, Week, Workday

@receiver(post_save, sender=Schedule)
def create_schedule(sender, instance, created, **kwargs):
    if created:
        instance.employees.set(instance.team.employee_set.filter(active=True))
        for i in range(instance.team.n_periods):
            instance.periods.create(number=i)

@receiver(post_save, sender=Period)
def create_period(sender, instance, created, **kwargs):
    if created:
        for i in range(2):
            instance.weeks.create(number=i)
            
@receiver(post_save, sender=Week)
def create_week(sender, instance, created, **kwargs):
    if created:
        for i in range(7):
            instance.workdays.create(number=i)

@receiver(post_save, sender=Workday)
def create_workday(sender, instance, created, **kwargs):
    if created:
        for s in instance.schedule.team.shift_set.filter(weekdays=instance.date.weekday()):
            instance.slots.create(shift=s)
