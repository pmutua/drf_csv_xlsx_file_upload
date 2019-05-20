from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from patients import views

urlpatterns = [
    re_path(r'^upload/(?P<filename>[^/]+)$', views.FileUploadView.as_view())
]
