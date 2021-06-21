import glob
import json
import time


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

    def save(self, files_content, format_):

        for f_content in files_content:

            files_next_count = len(glob.glob(f"../output/{format_}/*_file*.json")) + 1

            f_content.update({"file_name": self.files[0]})
            f_content.move_to_end('file_name', last=False)

            write_file = self.open_file(f'{time.time()}_file{files_next_count}.json', 'w')
            json.dump(f_content, write_file, indent=3, separators=(',', ':'))
