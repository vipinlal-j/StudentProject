from rest_framework import serializers
from StudApp.models import StudentDB

class Student_Serializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDB
        fields = (
            'StudID',
            'Name',
            'Age',
            'Place',
            'Course',
            'Address'
        )