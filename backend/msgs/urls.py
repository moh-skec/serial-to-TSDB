from django.urls import path
from .views import MsgView

urlpatterns = [
    path('', MsgView.as_view()),
    path('<int:msg_id>/', MsgView.as_view(), name='msg-detail'),
]
