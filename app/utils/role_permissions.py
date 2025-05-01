from typing import Set, Dict
from app.models.user import RoleEnum
from fastapi import Depends,HTTPException
from app.schemas.user import User
from .enums import RoleEnum, PermissionEnum
from app.utils.get_current_user import get_current_user



ROLE_PERMISSIONS: Dict[RoleEnum, Set[PermissionEnum]] = {
    RoleEnum.ADMIN: { PermissionEnum.create_project, PermissionEnum.view_project },
    RoleEnum.USER:{ PermissionEnum.view_project }
   
}

def require_permission(permission: PermissionEnum):
    def checker(user: User = Depends(get_current_user)) -> User:
        permissions = ROLE_PERMISSIONS.get(user.role, set())
        if permission not in permissions:
            raise HTTPException(status_code=403, detail="Permission denied")
        return user
    return checker