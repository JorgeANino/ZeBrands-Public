from .core.constants import Constants


class Roles(Constants):
    """Roles allowed in the platform"""

    class Meta:
        hidden_constants = ["ALL_ROLES"]

    ADMIN = "Admin"
    ALL_ROLES = "*"


class AllowedActions(Constants):
    RETRIEVE = "retrieve"
    CREATE = "create"
    UPDATE = "update"
    PARTIAL_UPDATE = "partial_update"
    DESTROY = "destroy"
    LIST = "list"

    # Custom actions
    ME = "me"
    FORCE = "force"
