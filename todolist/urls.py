from django.contrib import admin
from django.urls import path, include
from todo.views import home
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', home, name='home'),  # Root homepage
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),  # Todo API routes
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh
]
