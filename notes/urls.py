from django.urls import path
from .views import NoteList, NoteCreate, NoteDetail, NoteUpdate, NoteDelete, SignupView, LogoutView
from rest_framework.authtoken import views  # for login
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView





urlpatterns = [
    path('notes/', NoteList.as_view(), name='note-list'),
    path('notes/create/', NoteCreate.as_view(), name='note-create'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
    path('notes/update/<int:pk>/', NoteUpdate.as_view(), name='note-update'),
    path('notes/delete/<int:pk>/', NoteDelete.as_view(), name='note-delete'),

    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', views.obtain_auth_token, name='login'), #token auth endpoint
    path('logout/', LogoutView.as_view(), name='logout'), #token auth
]
urlpatterns += [
    path('jwt/', TokenObtainPairView.as_view(), name='jwt_login'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
]
