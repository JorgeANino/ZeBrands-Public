from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication

from catalog_system.constants import AllowedActions
from .permissions import CatalogSystemModelPermission

ACTION_MAPPING = {
    "get": AllowedActions.RETRIEVE,
    "post": AllowedActions.CREATE,
    "put": AllowedActions.UPDATE,
    "patch": AllowedActions.PARTIAL_UPDATE,
    "delete": AllowedActions.DESTROY,
}


class PermissionsMixin:
    """Permission class to specify permissions on views"""

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated, CatalogSystemModelPermission)
    custom_action_map = {}

    @property
    def view_name(self):
        """Returns the name of the class"""
        return "{}.{}".format(
            self.__class__.__module__.split(".")[0], self.__class__.__name__
        )

    @property
    def _action(self):
        """Returns an action depending on the request method specified"""
        if hasattr(self, "action") and self.action:
            return self.custom_action_map.get(self.action, self.action)
        return ACTION_MAPPING[self.request.method.lower()]


class CatalogSystemModelViewset(PermissionsMixin, ModelViewSet):
    read_serializer = None
    write_serializer = None

    def get_serializer_class(self, *args, **kwargs):
        """Gets the serializer class depending on the type of action"""
        if (
            self.action in (AllowedActions.RETRIEVE, AllowedActions.LIST)
            and self.read_serializer
        ):
            return self.read_serializer
        elif (
            self.action
            in (
                AllowedActions.CREATE,
                AllowedActions.UPDATE,
                AllowedActions.PARTIAL_UPDATE,
            )
            and self.write_serializer
        ):
            return self.write_serializer
        return super().get_serializer_class(*args, **kwargs)
