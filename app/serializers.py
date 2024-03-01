from .models import Student
from rest_framework import serializers

# Validators outside the serializers 1 priority
def start_with_y(value):
    if value[0].lower() != 'y':
        raise serializers.ValidationError('Name must be start with Y')

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, validators=[start_with_y])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = "__all__"


# Validation for roll syntax: def validate_fieldname(self, value)  called Fieldlevel Validation 2nd priority
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value

# Object Level Validation 3rd priority
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'suniyo' and ct.lower() != 'ranchi': # raised error bcs in myapp city is not ranchi
            raise serializers.ValidationError('City must be Ranchi')
        return data

