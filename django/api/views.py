from datetime import datetime
from django.shortcuts import render

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Exercise, Workout
from .serializers import AuthSerializer, ExerciseSerializer, UserSerializer, WorkoutSerializer
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class WorkoutListView(generics.ListCreateAPIView):
#     serializer_class = WorkoutSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Workout.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
    
class WorkoutList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        start_date_str = self.request.query_params.get('start_date')
        end_date_str = self.request.query_params.get('end_date')

        if not start_date_str or not end_date_str:
            return Response({"error": "Both start_date and end_date parameters are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({"error": "Invalid date format. Please use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        workouts = Workout.objects.filter(date__range=[start_date, end_date], user=self.request.user)
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data)
    
class ExerciseList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        workout_id = self.request.query_params.get('workout_id')

        if not workout_id:
            return Response({"error": "workout_id parameter is required."}, status=status.HTTP_400_BAD_REQUEST)


        workout = Workout.objects.get(id=workout_id)
        if workout.user != self.request.user:
            return Response({"error": "You do not have permission to view this workout."}, status=status.HTTP_403_FORBIDDEN)
        exercises = Exercise.objects.filter(workout=workout)
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)

        
# class WorkoutView(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request, *args, **kwargs):
        
#         return Response({}, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):
#         return Response({}, status=status.HTTP_201_CREATED)
    
#     def put(self, request, *args, **kwargs):
#         return Response({}, status=status.HTTP_200_OK)
    
#     def delete(self, request, *args, **kwargs):
#         return Response({}, status=status.HTTP_204_NO_CONTENT)