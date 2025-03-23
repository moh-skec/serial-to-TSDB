from django.urls import path
from .views import UserProfileView

urlpatterns = [
    path('', UserProfileView.as_view()),
    path('<int:user_id>/', UserProfileView.as_view()),
]
