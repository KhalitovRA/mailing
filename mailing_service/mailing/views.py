from django.shortcuts import render, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, generics

from .models import Mailing, Client, Message
from .serializers import MailingSerializer, ClientSerializer, MessageSerializer


class ClientViewSet(viewsets.ModelViewSet):
    '''
    Добавление нового клиента в справочник
    '''
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def perform_create(self, serializer):
        serializer.save(phone_number=self.request)


class ClientAPIUpdate(generics.RetrieveUpdateAPIView):
    '''Обновление данных атрибутов клиента'''
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )


class MailingAPIUpdate(generics.RetrieveUpdateAPIView):
    '''Добавление новой рассылки со всеми её атрибутами'''
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
    permission_classes = (IsAuthenticated, )


class ClientAPIDestroy(generics.RetrieveDestroyAPIView):
    '''Удаление клиента из справочника'''
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated, )


class MailingAPIDestroy(generics.RetrieveDestroyAPIView):
    '''Удаление рассылки'''
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
    permission_classes = (IsAuthenticated, )


class MessageViewSet(viewsets.ModelViewSet):

    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    queryset = Mailing.objects.all()

