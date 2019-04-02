class UserNotFoundError(Exception):
    """Raise the exception when user not found."""
    def __init__(self, message=None, erros=None):
        # Calling the base class constructor with the parameter it needs
        super().__init__(message)
        # New for your custom code
        self.errors = errors


def get_user_info(user_obj):
    """Get user information from DB."""
    user = get_user_from_db(user_obj)
    if not user:
        raise UserNotFoundException(f"No user found of this id: {user_obj.id}")

get_user_info(user_obj)

"""
>>> UserNotFoundException: No user found of this id: 897867
"""
