class FileHandler:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

    def read_file(self):
        print("Reading file: {}".format(self.source))
        with open(self.source, 'r') as file:
            return file.read()

    def write_file(self, content):
        print("Writing to file: {}".format(self.dest))
        with open(self.dest, 'w') as file:
            file.write(content)


f1 = FileHandler("data.txt", "output.txt")
print(f1.read_file())                   