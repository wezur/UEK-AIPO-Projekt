from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from kernel import settings



class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, null=False, blank=True)

    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'
    LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (ADVANCED, 'Advanced'),
    ]
    level_of_advancement = models.CharField(max_length=20, choices=LEVEL_CHOICES, null=False, blank=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to their groups.'),
        related_name='custom_user_set'
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_set',
    )

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    date_recorded = models.DateTimeField(default=now, editable=False)

class RepeatingWorkout(models.Model):
    starting_date = models.DateField()
    ending_date = models.DateField()
    frequency = models.PositiveIntegerField()

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    repeatingWorkout = models.ForeignKey(RepeatingWorkout, on_delete=models.DO_NOTHING, null=True, blank=True)
    date = models.DateField()
    name = models.CharField(max_length=10, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.date}'
    
class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    description = models.TextField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    completed = models.BooleanField(default=False)
    date_completed = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.description