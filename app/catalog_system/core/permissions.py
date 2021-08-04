from rest_framework.permissions import BasePermission

from collections import defaultdict

from catalog_system.constants import Roles

from catalog_system.catalog.permissions import CATALOG_PERMISSIONS
from catalog_system.user.permissions import USER_PERMISSIONS


# Dictionary with all of the apps permissions
PERMISSIONS = defaultdict(
    dict,
    {
        **CATALOG_PERMISSIONS,
        **USER_PERMISSIONS,
    },
)


class CatalogSystemModelPermission(BasePermission):
    """Base CatalogSystem Permission"""

    def has_permission(self, request, view):
        """Checks if the role has permissions for the view specified"""
        view_permission = PERMISSIONS[view.view_name]
        valid_roles = [Roles.ALL_ROLES]
        valid_roles.extend(request.user.groups.values_list("name", flat=True))
        valid_actions = []
        for role in valid_roles:
            valid_actions.extend(
                view_permission.get(role, {}).get("actions", [])
            )
        return view._action in valid_actions
