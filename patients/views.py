from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from .serializers import PatientSerializer, PatientCreateSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing patients.
    """
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        """Return patients created by the authenticated user."""
        return Patient.objects.filter(created_by=self.request.user)
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'create':
            return PatientCreateSerializer
        return PatientSerializer
    
    def perform_create(self, serializer):
        """Set the created_by field to the current user."""
        serializer.save(created_by=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        """Override destroy to ensure proper deletion."""
        try:
            patient_id = kwargs.get('pk')
            
            try:
                # print("hello")
                instance = self.get_object()
            except Exception as e:
                return Response(
                    {
                        'error': f'Patient not found or access denied. Error: {str(e)}',
                        'patient_id': patient_id,
                        'user_id': request.user.id
                    }, 
                    status=status.HTTP_404_NOT_FOUND
                )
            # print("hello")

            patient_id = instance.id
            patient_name = instance.name
            
            # Actually delete the object
            instance.delete()
            
            return Response(
                {
                    'message': f'Patient "{patient_name}" (ID: {patient_id}) has been successfully deleted.'
                }, 
                status=status.HTTP_200_OK
            )
            
        except Exception as e:
            return Response(
                {
                    'error': f'Unexpected error during deletion: {str(e)}',
                    'patient_id': kwargs.get('pk'),
                    'user_id': request.user.id
                }, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )