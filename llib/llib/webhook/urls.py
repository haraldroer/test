from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #path('', views.index),
    #path('41d4b981-4522-45cb-b5db-36199aa719c2/', views.webhook),

    url(r'^41d4b981-4522-45cb-b5db-36199aa719c2$', views.index, name='index'),
    #url(r'^41d4b981-4522-45cb-b5db-36199aa719c2/$', views.webhook, name='webhook'),
]