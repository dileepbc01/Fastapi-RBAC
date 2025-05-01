from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"


class PermissionEnum(str, Enum):
    create_project="create_project"
    view_project="view_project"


class LogLevelEnum(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"
    
class AppEnvironmentEnum(str, Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    TESTING = "testing"