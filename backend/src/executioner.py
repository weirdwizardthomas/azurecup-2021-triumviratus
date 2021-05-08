import os

import template


class Executioner:
    """
    Wrapper around file deleting. Just wanted to be fancy, really.
    """

    @staticmethod
    def remove(file):
        """
        Deletes a file, if it exists.
        :param file: File to delete.
        :return: None
        """
        if os.path.exists(file):
            os.remove(file)
        else:
            print(template.FILE_NOT_FOUND_MESSAGE.format(file))
