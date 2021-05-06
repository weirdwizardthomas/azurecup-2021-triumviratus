import os

from src import template


class Executioner:
    def remove(self, file):
        if os.path.exists(file):
            os.remove(file)
        else:
            print(template.FILE_NOT_FOUND_MESSAGE.format(file))
