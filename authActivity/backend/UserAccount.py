class UserAccount:
    def __init__(self):
        self.accounts = {}
        self.current_user = None

    def register(self, username, password):
        if len(password) < 6:
            return "Password should be at least 6 characters"

        if username in self.accounts:
            return "User already exists"
        
        self.accounts[username] = password
        return "Registration successful"

    def login(self, username, password):
        if username in self.accounts and self.accounts[username] == password:
            self.current_user = username
            return "Login successful"
        elif username in self.accounts:
            return "Wrong password"
        else:
            return "User not found"
