from rest_framework import viewsets
from rest_framework.response import Response
from django.core.mail import send_mail

from . import serializers
from . import models

# Create your views here.

# email_sender/views.py

class MessageViewsets(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sender = serializer.validated_data['sender']
        receiver = serializer.validated_data['receiver'].split(',')
        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']
        
        
        send_mail(subject ,message ,sender ,receiver)
        
        serializer.save()
        return Response(serializer.data)