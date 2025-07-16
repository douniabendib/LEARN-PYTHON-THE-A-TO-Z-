# Create classes that implement the same interface but aren't related
class TextFile:
    def read(self):
        return "Reading text data"

    def write(self, data):
        return f"Writing text: {data}"


class Database:
    def read(self):
        return "Reading database records"

    def write(self, data):
        return f"Inserting record: {data}"


class NetworkResource:
    def read(self):
        return "Reading network data"

    def write(self, data):
        return f"Sending data: {data}"


def process_data(data_source, data):
    print(data_source.read())
    print(data_source.write(data))


# Test with different data sources 
text_file = TextFile()
database = Database()
network = NetworkResource()

print("Processing text file:")
process_data(text_file, "Hello, world!")

print("\nProcessing database:")
process_data(database, "User record")

print("\nProcessing network resource:")
process_data(network, "GET request")
