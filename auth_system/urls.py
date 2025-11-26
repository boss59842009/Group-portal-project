from django.urls import path
from .views import RegisterView, UserLoginView, UserLogoutView, ProfileView, ProfileEditView, UsersListView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/<int:pk>/", ProfileView.as_view(), name="profile"),
    path("profile/edit/<int:pk>", ProfileEditView.as_view(), name="profile_edit"),
    path("users/", UsersListView.as_view(), name="users_list"),
]