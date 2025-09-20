from rest_framework import serializers
from .models import Patient
from accounts.serializers import UserSerializer


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for Patient model.
    """
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Patient
        fields = ('id', 'name', 'age', 'gender', 'created_by', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_by', 'created_at', 'updated_at')


class PatientCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating patients.
    """
    class Meta:
        model = Patient
        fields = ('name', 'age', 'gender')
    
    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)