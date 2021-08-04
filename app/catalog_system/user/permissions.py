from catalog_system.constants import Roles, AllowedActions


USER_PERMISSIONS = {
    "catalog_system.UserView": {
        Roles.ALL_ROLES: {"actions": [AllowedActions.ME]},
        Roles.ADMIN: {
            "actions": [
                AllowedActions.RETRIEVE,
                AllowedActions.LIST,
                AllowedActions.CREATE,
                AllowedActions.UPDATE,
                AllowedActions.PARTIAL_UPDATE,
                AllowedActions.DESTROY,
            ]
        },
    },
}
