from django.urls import path

from . import views

urlpatterns = [
    path("stk/", views.SendSTKPushView.as_view(), name="stk"),
    path("callback/", views.MpesaCallbackView.as_view(), name="callback"),
    path("transactions/", views.TransactionView.as_view(), name="transactions")
]