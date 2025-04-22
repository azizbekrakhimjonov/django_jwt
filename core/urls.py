from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import RegisterView, MyTokenObtainPairView, UserListView, UserDetailView
from api.views import PostListCreateView, PostRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Auth URLs
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # User URLs
    path('api/users/', UserListView.as_view(), name='user-list'),
    path('api/users/<int:id>/', UserDetailView.as_view(), name='user-detail'),
    
    # Post URLs
    path('api/posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-retrieve-update-destroy'),
]