import pytz
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Mailing(models.Model):

    text = models.TextField('Сообщение', max_length=255)
    tag = models.CharField('Тег', max_length=100, blank=True)
    operator_code = models.CharField('Код мобильного оператора', max_length=3, blank=True)
    date_start = models.DateTimeField('Начало рассылки')
    date_end = models.DateTimeField('Конец рассылки')


class Client(models.Model):
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    phone_number = PhoneNumberField('Номер телефона', unique=True, null=False, blank=False, region='RU')
    mobile_code = models.CharField('Мобильный оператор', max_length=3)
    tag = models.CharField('Тег (произвольная метка)', max_length=100, blank=True)
    timezone = models.CharField('Часовой пояс', max_length=32, choices=TIMEZONES, default='UTC')


class Message(models.Model):
    SENT = "sent"
    NO_SENT = "no sent"

    STATUS_CHOICES = [
        (SENT, "Sent"),
        (NO_SENT, "No sent"),
    ]

    time_create = models.DateTimeField('Дата и время отправки', auto_now_add=True)
    sending_status = models.CharField('Статус отправки', max_length=15, choices=STATUS_CHOICES)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages')
