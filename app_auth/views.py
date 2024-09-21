from utilitas.views import BaseDetailsView, BaseListView, BaseSearchView, BaseView
from app_auth import models, serializers


class UserListView(BaseListView):
    model = models.User
    serializer = serializers.UserSerializer
    authentication_classes = []
    permission_classes = []


class UserDetailsView(BaseDetailsView):
    model = models.User
    serializer = serializers.UserSerializer
    authentication_classes = []
    permission_classes = []


class UserSearchView(BaseSearchView):
    model = models.User
    serializer = serializers.UserSerializer
    authentication_classes = []
    permission_classes = []
