from django.urls import path, include
from django.conf.urls import url
from core.views import (
    home,
)

urlpatterns = [
    path('', home, name='home'),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
]
