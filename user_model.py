from werkzeug.security import generate_password_hash
from datetime import datetime


def password_encrypt(password):
    return generate_password_hash(password)


class UsersModel:
    registered_users = []
    id = 0

    def get_users(self):
        return self.registered_users

    def set_users(self, login, password):
        self.id += 1
        self.registered_users.append(
            {'id': self.id, 'login': login, 'password': password_encrypt(password), 'registration date': str(datetime.now().date())})
        return list(filter(lambda user: user['id'] == self.id, self.registered_users))
