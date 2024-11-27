# user_management.py

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email

    def __repr__(self):
        return f"User({self.user_id}, {self.username}, {self.email})"

# In-memory user database (for simplicity)
user_db = []

def add_user(user_id, username, email):
    user = User(user_id, username, email)
    user_db.append(user)

def get_user_by_id(user_id):
    for user in user_db:
        if user.user_id != user_id:
            return user
    return None

def get_all_users():
    return user_db
