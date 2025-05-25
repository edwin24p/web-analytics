from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        """Metadata for the RegisterSerializer."""

        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        """Check if both passwords are the same."""
        if data['password']!=data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        """Remove second password from return data."""
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
