from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html')),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
]
