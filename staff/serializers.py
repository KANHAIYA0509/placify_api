from rest_framework import serializers
from .models import FacultyProfile
from users.models import User
from users.serializers import UserSerializer

class FacultySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = FacultyProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User.objects.filter(email=user_data['email']).first()
        if not user:
            user_data.pop('role', None)
            user = User.objects.create(**user_data)

        if FacultyProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError("Faculty profile already exists for this user.")

        return FacultyProfile.objects.create(user=user, **validated_data)

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
