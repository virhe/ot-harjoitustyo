from src.entities.user import User


class UserRepository:
    """
    Responsible for database operations related to the User class.

    Attributes:
        session (sqlalchemy.orm.Session): SQLAlchemy ORM Session object.
                                            Mostly to make testing easier.
    """

    def __init__(self, session):
        self.session = session

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()

    # def delete_user(self, user_id):
    #     user = self.find_user_id(user_id)
    #     self.session.delete(user)
    #     self.session.commit()

    def find_user_id(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        return user

    def find_user_name(self, username):
        user = self.session.query(User).filter_by(username=username).first()
        return user
