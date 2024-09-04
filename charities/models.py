from django.db import models
from django.db.models import SmallIntegerField, PositiveSmallIntegerField, IntegerField


class Charity(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class Benefactor(models.Model):
    EXPERIENCE_CHOICES = [
        (0, 'No Experience'),
        (1, 'Some Experience'),
        (2, 'Experienced'),
    ]

    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    experience = SmallIntegerField(choices=EXPERIENCE_CHOICES, default=0)
    free_time_per_week = PositiveSmallIntegerField(default=0)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        return self.filter(
            models.Q(charity__user=user) | models.Q(assigned_benefactor__user=user) | models.Q(state='P'))


class Task(models.Model):
    GENDER_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]

    STATE_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Assigned'),
        ('W', 'Waiting'),
        ('D', 'Done'),
    ]

    assigned_benefactor = models.ForeignKey('Benefactor', on_delete=models.SET_NULL, null=True)
    charity = models.ForeignKey('Charity', on_delete=models.CASCADE)
    age_limit_from = IntegerField(blank=True, null=True)
    age_limit_to = IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender_limit = models.CharField(choices=GENDER_CHOICES, blank=True, null=True, max_length=1)
    state = models.CharField(choices=STATE_CHOICES, default='P', max_length=1)
    title = models.CharField(max_length=60)

    objects = TaskManager()
