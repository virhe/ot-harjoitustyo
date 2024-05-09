from src.entities.user import User


class UserRepository:
    """Responsible for database operations related to the User class"""

    def __init__(self, session):
        """Constructor

        Args:
            session: sqlalchemy session
        """

        self.session = session

    def add_user(self, user):
        """Adds a new user to the database

        Args:
            user: User instance

        Returns:
            user.id: id of the added user
        """

        self.session.add(user)
        self.session.commit()
        return user.id

    def find_user_name(self, username):
        """Returns user with given username

        Args:
            username: username to be looked for in the database

        Returns:
            user: User instance of the user with the given username
        """

        user = self.session.query(User).filter_by(username=username).first()
        return user
