from django.urls import path

from .views import PdfAsyncView, PdfWebsocketView

urlpatterns = [
    path('socket/', PdfWebsocketView.as_view()),
    path('async/', PdfAsyncView.as_view()),
]
