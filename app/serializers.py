from .models import Student
from rest_framework import serializers

# Validators outside the serializers 1 priority
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'