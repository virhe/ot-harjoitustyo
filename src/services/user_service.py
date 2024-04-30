import bcrypt

from src.entities.user import User


class UserService:
    """Responsible for the logic related to users
    """

    def __init__(self, user_repository):
        """Constructor

        Args:
            user_repository: user_repository instance
        """

        self.user_repository = user_repository

    def login(self, username, password):
        """Handles user login

        Args:
            username: username of the user
            password: password of the user

        Returns:
            user.id: id of the user (on success)
            None: on failure
        """

        user = self.user_repository.find_user_name(username)
        if user and bcrypt.checkpw(
            password.encode("utf-8"), user.password.encode("utf-8")
        ):
            return user.id

        return None

    def register(self, username, password):
        """Handles user registration

        Args:
            username: username of the user
            password: password of the user

        Raises:
            UsernameTakenError: if the username is already taken
            InvalidUsernameOrPassword: if the username or password is under 3 characters long

        Returns:
            user.id: id of the added user
        """

        if self.user_repository.find_user_name(username):
            raise UsernameTakenError("User with given username already exists")

        if len(username) < 3 or len(password) < 3:
            raise InvalidUsernameOrPassword(
                "Username and password must be at least 3 characters long"
            )

        user = User(username=username, password=hash_pw(password))
        self.user_repository.add_user(user)

        return self.user_repository.add_user(user)


# Not a course requirement, but a good practice
def hash_pw(password):
    """Hashes the given password

    Args:
        password: password to be hashed

    Returns:
        Hashed password
    """

    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


class UsernameTakenError(Exception):
    """Custom exception for when a username is taken
    """
    pass


class InvalidUsernameOrPassword(Exception):
    """Custom exception for when a username or password is under 3 characters long
    """
    pass
