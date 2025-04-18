from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("webauthn/", include("django_otp_webauthn.urls", namespace="otp_webauthn")),
]
