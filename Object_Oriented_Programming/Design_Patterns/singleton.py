"""
Create a class named DatabaseConnection that implements the Singleton pattern. 
The class should:

Have a private class variable _instance initialized to None
Override the __new__ method to ensure only one instance is created
Have an __init__ method that initializes instance variables host 
to "localhost" and connected to False
Have a connect method that sets connected to True 
and prints "Connected to database at localhost"
Have a disconnect method that sets connected to False 
and prints "Disconnected from database"
"""
class DatabaseConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self.host = "localhost"
        self.connected = False
    
    def connect(self):
        self.connected = True
        print("Connected to database at localhost")
    
    def disconnect(self):
        self.connected = False
        print("Disconnected from database")


# Attempt to create multiple instances
db1 = DatabaseConnection()
db2 = DatabaseConnection()

# Check if both variables point to the same instance
print(db1 is db2)  # Should print True

# Connect to the database
db1.connect()  # Output: Connected to database at localhost

# Attempt to connect again
db2.connect()  # Output: Already connected to the database.

# Disconnect from the database
db1.disconnect()  # Output: Disconnected from database

# Attempt to disconnect again
db2.disconnect()  # Output: No connection to disconnect.
