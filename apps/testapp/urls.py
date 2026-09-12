from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
import apps.testapp.views


urlpatterns = [
    path('register/', apps.testapp.views.RegisterView.as_view(), name='register'),
    path('token/', apps.testapp.views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('public/', apps.testapp.views.PublicDataView.as_view(), name='public-data'),
    path('secret/', apps.testapp.views.SecretModeratorView.as_view(), name='secret-data'),
    path('google/', apps.testapp.views.GoogleAuthView.as_view(), name='google_auth'),
]


