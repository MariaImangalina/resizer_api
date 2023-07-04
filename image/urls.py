from django.urls import path
from .views import ImageAPIView

app_name = 'image'

urlpatterns = [
    path("", ImageAPIView.as_view(), name="resize"),
]
