from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = format_suffix_patterns([
    path('client/', views.ClientViewSet.as_view({'post': 'create'})),
    path('client/<int:pk>/', views.ClientAPIUpdate.as_view()),
    path('clientdelete/<int:pk>/', views.ClientAPIDestroy.as_view()),
    path('messages/', views.MessageViewSet.as_view({'get': 'list'})),
    path('mailing/', views.MailingViewSet.as_view({'post': 'create'})),
    path('mailing/<int:pk>/', views.MailingAPIUpdate.as_view()),
    path('mailingdelete/<int:pk>/', views.MailingAPIDestroy.as_view()),
    # path('mailings/info', views.MailingViewSet.as_view({'get': 'info'})),
    # path('mailings/fullinfo', views.MailingViewSet.as_view({'get': 'fullinfo'})),
])
