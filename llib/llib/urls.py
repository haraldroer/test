from django.conf.urls import include
from django.urls import path
urlpatterns =[
    path('',include('llib.instruction.urls')),
    path('webhook/',include('llib.webhook.urls')),
]