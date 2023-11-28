import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        key = hashlib.sha256(website.encode()).hexdigest()
        self.passwords[key] = (website, username, password)

    def get_password(self, website):
        key = hashlib.sha256(website.encode()).hexdigest()
        if key in self.passwords:
            return self.passwords[key]
        else:
            return None

# Example usage
password_manager = PasswordManager()

# Add passwords
password_manager.add_password("example.com", "user1", "password123")
password_manager.add_password("google.com", "user2", "securepass")

# Get passwords
print(password_manager.get_password("example.com"))  # Output: ('example.com', 'user1', 'password123')
print(password_manager.get_password("google.com"))   # Output: ('google.com', 'user2', 'securepass')
print(password_manager.get_password("facebook.com")) # Output: None