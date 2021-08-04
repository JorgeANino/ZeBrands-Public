from catalog_system.constants import Roles, AllowedActions


CATALOG_PERMISSIONS = {
    "catalog_system.ProductView": {
        Roles.ALL_ROLES: {"actions": [AllowedActions.LIST, AllowedActions.RETRIEVE]},
        Roles.ADMIN: {
            "actions": [
                AllowedActions.CREATE,
                AllowedActions.UPDATE,
                AllowedActions.PARTIAL_UPDATE,
                AllowedActions.DESTROY,
            ]
        },
    },
}
