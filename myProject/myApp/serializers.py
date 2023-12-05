from rest_framework import serializers

class Student_Serializer(serializers.Serializer):
    Name=serializers.CharField(max_length=100)
    Roll=serializers.CharField(max_length=100)
    Department=serializers.CharField(max_length=100)