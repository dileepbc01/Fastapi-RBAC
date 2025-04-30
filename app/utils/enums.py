from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class PermissionEnum(str, Enum):
    create_project="create_project"
    view_project="view_project"
