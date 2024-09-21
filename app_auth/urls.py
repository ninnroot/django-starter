
from django.urls import path
from app_auth import views

urlpatterns = [
    path("users", views.UserListView.as_view(), name="user-list"),
    path("users/<int:obj_id>", views.UserDetailsView.as_view(), name="user-details"),
    path("users/search", views.UserSearchView.as_view(), name="user-search"),
]