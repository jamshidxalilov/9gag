from django.urls import path
from .views import MainIndex, UploadPost

app_name = 'main'
urlpatterns = [
    path('', MainIndex.as_view(), name='index'),
    path('cat/<int:id>', MainIndex.as_view(), name='cat'),
    path('upload/', UploadPost.as_view(), name='upload')
]
