class SecureMessenger:
    def __init__(self, username, password="secure123"):
        self.username = username  # Public attribute
        self.__user_password = password  # Private attribute
        self.__messages = []  # Private list to store messages
        self.__logged_in = False  # Private attribute to track login status
        self.__login_attempts = 0  # Private attribute to count login attempts

    def add_message(self, message):
        if self.__logged_in:
            if message:
                self.__messages.append(message)  # Store the message
                return f"Message added: {message}"
            return "Error: Message cannot be empty"
        return "Error: You must be logged in to add messages"

    def login(self, password):
        self.__login_attempts += 1  # Increment login attempts
        if self.__user_password == password:
            self.__logged_in = True  # Set login status
            return "Login successful"
        else:
            return "Login failed: Incorrect password"

    def get_messages(self):
        if self.__logged_in:
            if self.__messages:
                return "\n".join(self.__messages)  # Return all messages
            return "No messages"
        return "Error: You must be logged in to view messages"

    def get_login_attempts(self):
        return f"Login attempts: {self.__login_attempts}"


# Test the SecureMessenger 
messenger = SecureMessenger("user1")

# Try to add messages before login
print(messenger.add_message("Hello World!"))
print(messenger.add_message("Secure Message"))

# Attempt login with wrong password
print(messenger.login("wrong_pass"))

# Login with correct password
print(messenger.login("secure123"))

# Add messages after successful login
print(messenger.add_message("Hello World!"))
print(messenger.add_message("Secure Message"))

# Retrieve messages
print(messenger.get_messages())

# Check login attempts
print(messenger.get_login_attempts())
