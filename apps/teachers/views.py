from rest_framework import viewsets
from apps.users.permissions import IsAdmin
from .models import Teacher
from .serializers import TeacherSerializer, TeacherCreateSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.select_related('user').all()
    permission_classes = [IsAdmin]

    def get_serializer_class(self):
        if self.action == 'create':
            return TeacherCreateSerializer
        return TeacherSerializer