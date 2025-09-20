from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingCreateSerializer
from patients.models import Patient


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing patient-doctor mappings.
    """
    queryset = PatientDoctorMapping.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return PatientDoctorMappingCreateSerializer
        return PatientDoctorMappingSerializer
    
    def list(self, request, *args, **kwargs):
        """
        List all patient-doctor mappings.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        """
        Create a new patient-doctor mapping.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a specific mapping.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        """
        Delete a patient-doctor mapping.
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def get_doctors_for_patient(self, request, patient_id=None):
        """
        Get all doctors assigned to a specific patient.
        """
        try:
            patient = get_object_or_404(Patient, id=patient_id)
            mappings = self.get_queryset().filter(patient=patient)
            serializer = self.get_serializer(mappings, many=True)
            return Response(serializer.data)
        except ValueError:
            return Response(
                {'error': 'Invalid patient ID'}, 
                status=status.HTTP_400_BAD_REQUEST
            )