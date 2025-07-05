from rest_framework import serializers
from .models import StudentProfile
from users.models import User
from users.serializers import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = StudentProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User.objects.filter(email=user_data['email']).first()
        if not user:
            user_data.pop('role', None)
            user = User.objects.create(**user_data)

        if StudentProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError("Student profile already exists for this user.")

        return StudentProfile.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        if user_data:
            user = instance.user
            for attr, value in user_data.items():
                setattr(user, attr, value)
            user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
