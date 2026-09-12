from rest_framework.permissions import BasePermission
from apps.testapp.models import CustomUser


class IsModeratorOrAdmin(BasePermission):
    """
    Разрешает доступ только пользователям с ролью MODERATOR или ADMIN.
    """
    def has_permission(self, request, view):
        # 1. Проверяем, залогинен ли пользователь вообще
        if not request.user or not request.user.is_authenticated:
            return False

        # 2. Проверяем, подходит ли его роль
        return request.user.role in [CustomUser.Role.MODERATOR, CustomUser.Role.ADMIN]