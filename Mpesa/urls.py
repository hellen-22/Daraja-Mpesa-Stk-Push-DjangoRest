from django.urls import path

from . import views

urlpatterns = [
    path("stk/", views.SendSTKPushView.as_view(), name="stk")
]