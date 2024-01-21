from django.contrib import admin

from .models import RepeatingWorkout, User, Workout, Exercise, UserProfile


admin.site.register(User)
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(UserProfile)
admin.site.register(RepeatingWorkout)