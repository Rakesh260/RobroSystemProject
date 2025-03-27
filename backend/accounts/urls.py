from django.urls import path
from .views import RegisterUserView,CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
    # path('create-user/', CreateUserView.as_view(), name='create-user'),
    # path('delete-user/<int:user_id>/', DeleteUserView.as_view(), name='delete-user'),
    # path('upload-image/', UploadImageView.as_view(), name='upload-image'),
    # path('user-images/', UserImagesView.as_view(), name='user-images'),
]
