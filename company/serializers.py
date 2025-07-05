from rest_framework import serializers
from .models import CompanyProfile
from users.models import User
from users.serializers import UserSerializer

class CompanySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = CompanyProfile
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user = User.objects.filter(email=user_data['email']).first()
        if not user:
            user_data.pop('role', None)
            user = User.objects.create(**user_data)

        if CompanyProfile.objects.filter(user=user).exists():
            raise serializers.ValidationError("Company profile already exists for this user.")

        return CompanyProfile.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        if user_data:
            user = instance.user
            for attr, value in user_data.items():
                # Safely handle password update
                if attr == 'password':
                    user.set_password(value)
                else:
                    # Only update if value is actually changed
                    if getattr(user, attr) != value:
                        setattr(user, attr, value)
            user.save()

        # Update CompanyProfile fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
