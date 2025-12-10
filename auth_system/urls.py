from django.urls import path

from .views import RegisterView, UserLoginView, UserLogoutView, ProfileView, ProfileEditView, UsersListView, UserListView, UserRoleUpdateView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("users/", UsersListView.as_view(), name="users_list"),
    path("admin/users/", UserListView.as_view(), name="admin-users-list"),
    path("admin/users/<int:pk>/edit/", UserRoleUpdateView.as_view(), name="admin-user-edit"),
]

