from src.entities.user import User
from src.database import session


class UserRepository:
    def __init__(self):
        self.session = session

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()

    def delete_user(self, user_id):
        user = self.get_user_id(user_id)
        self.session.delete(user)
        self.session.commit()

    def get_user_id(self, user_id):
        user = self.session.query(User).filter_by(id=user_id).first()
        return user
