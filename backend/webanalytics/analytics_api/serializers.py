from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
    def validate(self, data):
        if data['password']!=data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def create(self, validated_data):
        # We only needed the second password for validation purposes so we remove it from the validated data
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user