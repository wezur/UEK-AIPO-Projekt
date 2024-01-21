from rest_framework import serializers
from django.contrib.auth import get_user_model

from api.models import Exercise, UserProfile, Workout


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class AuthSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer()

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password', 'user_profile', 'email', 'first_name', 'last_name', 'sex', 'level_of_advancement', 'birth_date']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        print(validated_data)
        user_profile_data = validated_data.pop('user_profile', None)
        print(validated_data)
        user = get_user_model().objects.create_user(**validated_data)
        print(user)
        
        if user_profile_data:
            UserProfile.objects.create(user=user, **user_profile_data)
        
        return user
    

    def get_user(self, username, password):
        try:
            user = get_user_model().objects.get(username=username)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            pass

        return None
    
class UserSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(many=False, read_only=True)

    class Meta:
        model = get_user_model()
        fields = [ 'username', 'user_profile', 'first_name', 'last_name', 'sex', 'level_of_advancement', 'birth_date']



    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # repeatingWorkout = models.ForeignKey(RepeatingWorkout, on_delete=models.DO_NOTHING, null=True, blank=True)
    # date = models.DateField()
    # notes = models.TextField(blank=True)
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'repeatingWorkout', 'date', 'notes']
        depth = 1

    #         workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    # description = models.TextField()
    # sets = models.PositiveIntegerField()
    # reps = models.PositiveIntegerField()
    # completed = models.BooleanField(default=False)
    # date_completed = models.DateTimeField(null=True, blank=True)


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'description', 'sets', 'reps', 'completed', 'date_completed']