from django.shortcuts import render


from rest_framework import viewsets
from .models import Event
from .serializers import EventSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def perform_create(self, serializer):
        max_attendees = serializer.validated_data.get('max_attendees')
        if max_attendees <= 0:
            raise ValidationError("max_attendees must be greater than zero.")
        serializer.save()

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.prefetch_related('tickets').select_related('event')
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)