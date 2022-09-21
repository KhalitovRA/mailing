from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response

from .models import Mailing, Client, Message


class MailingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mailing
        fields = "__all__"

    def create(self, validated_data):
        client, _ = Mailing.objects.update_or_create(
            text=validated_data.get('text'),
            operator_code=validated_data.get('operator_code'),
            tag=validated_data.get('tag'),
            date_start=validated_data.get('date_start'),
            date_end=validated_data.get('date_end'),
        )
        return client

    def info(self, request, pk=None):
        """
        Summary data for a specific mailing list
        """
        maililng = Mailing.objects.get(pk=pk)
        return maililng

    def fullinfo(self, request):
        """
        Summary data for all mailings
        """
        total_count = Mailing.objects.count()
        mailing = Mailing.objects.values('id')
        content = {'Total number of mailings': total_count,
                   'The number of messages sent': ''}
        result = {}

        for row in mailing:
            res = {'Total messages': 0, 'Sent': 0, 'No sent': 0}
            mail = Message.objects.filter(mailing_id=row['id']).all()
            group_sent = mail.filter(sending_status='Sent').count()
            group_no_sent = mail.filter(sending_status='No sent').count()
            res['Total messages'] = len(mail)
            res['Sent'] = group_sent
            res['No sent'] = group_no_sent
            result[row['id']] = res

        content['The number of messages sent'] = result
        return Response(content)


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        client, _ = Client.objects.update_or_create(
            phone_number=validated_data.get('phone_number', None),
            mobile_code=validated_data.get('mobile_code'),
            tag=validated_data.get('tag'),
            timezone=validated_data.get('timezone', None),
        )
        return client


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
