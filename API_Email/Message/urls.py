# email_sender/urls.py
from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("send-mail", views.MessageViewsets)

urlpatterns = router.urls
