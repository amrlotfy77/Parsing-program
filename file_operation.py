

class FileOperation:

    def __init__(self, files):
        self.files = files
        self.files_content = []
        self.read_files()

    @staticmethod
    def open_file(path, state):
        return open(path, state)

    def read_files(self):
        for file in self.files:
            open_read_file = self.open_file(file, 'r')
            self.files_content.append(open_read_file)

    def get_content(self):
        return self.files_content