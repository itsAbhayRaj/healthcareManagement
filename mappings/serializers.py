from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    """
    Serializer for PatientDoctorMapping model.
    """
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)
    patient_id = serializers.IntegerField(write_only=True)
    doctor_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = PatientDoctorMapping
        fields = ('id', 'patient', 'doctor', 'patient_id', 'doctor_id', 'created_at')
        read_only_fields = ('id', 'created_at')
    
    def create(self, validated_data):
        patient_id = validated_data.pop('patient_id')
        doctor_id = validated_data.pop('doctor_id')
        
        from patients.models import Patient
        from doctors.models import Doctor
        
        try:
            patient = Patient.objects.get(id=patient_id)
            doctor = Doctor.objects.get(id=doctor_id)
        except (Patient.DoesNotExist, Doctor.DoesNotExist):
            raise serializers.ValidationError("Invalid patient or doctor ID.")
        
        validated_data['patient'] = patient
        validated_data['doctor'] = doctor
        
        return super().create(validated_data)


class PatientDoctorMappingCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating patient-doctor mappings.
    """
    class Meta:
        model = PatientDoctorMapping
        fields = ('patient', 'doctor')