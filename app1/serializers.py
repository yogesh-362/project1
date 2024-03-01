from .models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    # validation for single field below line
    # name = serializers.CharField(read_only=True)
    # Validators outside the serializers 1 priority
    def start_with_y(value):
        if value[0].lower() != 'y':
            raise serializers.ValidationError('Name must be start with Y')
    name = serializers.CharField(validators=[start_with_y])
    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name', 'roll'] # validation for multiple fields


    # filed level validation
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

    # object level validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'kenichi' and ct.lower() != 'ranchi': # raised error bcs in myapp city is not ranchi
            raise serializers.ValidationError('City must be Ranchi')
        return data
