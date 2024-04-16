import bcrypt

from src.entities.user import User


class UserService:
    """
    Responsible for managing all users.

    Attributes:
        user_repository: Handles database operations for all users.
    """

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def login(self, username, password):
        user = self.user_repository.find_user_name(username)
        if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return user.id

        return None

    def register(self, username, password):
        if self.user_repository.find_user_name(username):
            raise UsernameTakenError("User with given username already exists")

        if len(username) < 3 or len(password) < 3:
            raise InvalidUsernameOrPassword(
                "Username and password must be at least 3 characters long")

        user = User(username=username, password=hash_pw(password))
        self.user_repository.add_user(user)

        return user.id


def hash_pw(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


# Custom errors so pylint won't complain about "Exception"
class UsernameTakenError(Exception):
    pass


class InvalidUsernameOrPassword(Exception):
    pass
