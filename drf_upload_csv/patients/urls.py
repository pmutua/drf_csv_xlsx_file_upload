from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from patients import views

urlpatterns = [
    path(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view())
]
