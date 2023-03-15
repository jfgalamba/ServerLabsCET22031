__all__ = (
    'ViewModel',
)


from typing import Any

from common.fastapi_utils import global_request
from common.auth import get_auth_from_cookie


class ViewModel(dict):
    def __init__(self, *args, **kargs):
        user_id = get_auth_from_cookie(global_request.get())
        all = {
            'error': None,
            'error_msg': None,
            'user_id': user_id,
            'is_logged_in': user_id is not None,
        }
        all.update(kargs)
        super().__init__(self, *args, **all)
    #:

    def __getattr__(self, name: str) -> Any:
        return self[name]
    #:

    def __setattr__(self, name: str, value: Any):
        self[name] = value
    #:
#:  
