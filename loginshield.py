# loginshield/login.py

class LoginShield:
    def __init__(self):
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            return "User already exists."
        self.users[username] = password
        return "User added."

    def remove_user(self, username):
        if username in self.users:
            del self.users[username]
            return "User removed."
        return "User not found."

    def login(self, username, password):
        if self.users.get(username) == password:
            return "Login successful."
        return "Invalid username or password."

    def change_password(self, username, old_password, new_password):
        if self.users.get(username) == old_password:
            self.users[username] = new_password
            return "Password changed."
        return "Old password incorrect."

    def user_exists(self, username):
        return username in self.users

    def get_user_count(self):
        return len(self.users)

    def list_users(self):
        return list(self.users.keys())

    def reset_all_users(self):
        self.users.clear()
        return "All users removed."

    def validate_password_strength(self, password):
        if len(password) >= 8 and any(char.isdigit() for char in password):
            return "Strong password."
        return "Weak password. Must be at least 8 characters with a number."
