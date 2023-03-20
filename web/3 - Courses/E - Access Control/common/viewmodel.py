__all__ = (
    'ViewModel',
)


from typing import Any

from common.fastapi_utils import global_request
from common.auth import get_current_user


class ViewModel(dict):
    def __init__(self, *args, **kargs):
        user = get_current_user()
        user_id = user.id if user else None
        all = {
            'error': None,
            'error_msg': None,
            'user_id': user_id,
            'is_logged_in': user_id is not None,
        }
        all.update(kargs)
        super().__init__(*args, **all)
    #:

    def __getattr__(self, name: str) -> Any:
        return self[name]
    #:

    def __setattr__(self, name: str, value: Any):
        self[name] = value
    #:
#:  
