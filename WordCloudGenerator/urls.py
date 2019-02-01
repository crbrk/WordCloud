from django.urls import path
from .views import WordCloudGenerator

urlpatterns = [
    path('', WordCloudGenerator.as_view(), name='generator'),

]