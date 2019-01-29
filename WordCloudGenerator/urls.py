from django.urls import include
from django.urls import path
from .views import WordCloudGenerator
from .views import *

urlpatterns = [
    path('', WordCloudGenerator.as_view(), name='generator'),
    #path('test', recolor, name='recolor')
    #path('2', WordCloudGenerator2.as_view(), name='svg-gen'),
]