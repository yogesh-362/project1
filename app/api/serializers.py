from app.models import User
from rest_framework import serializers

class UserSearilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
