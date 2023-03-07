
def base_viewmodel():
    return {
        'error': None,
        'error_msg': None,
        'user_id': None,
        'is_logged_in': False,
    }
#:

def base_viewmodel_with(update_data: dict) -> dict:
    vm = base_viewmodel()
    vm.update(update_data)
    return vm
#: