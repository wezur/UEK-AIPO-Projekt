
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import ExerciseList, UserRegistrationView, WorkoutList

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('workouts/', WorkoutList.as_view(), name='workout_list'),
    path('exercises/', ExerciseList.as_view(), name='excercise_list')
    # Add other URLs as needed
]