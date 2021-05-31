import os

from werkzeug.utils import secure_filename
import template

from config import config


def read(file):
    """
    Reads a file from a POST request and stores it locally.
    :param file: POST request data.
    :return: str | Name of the file
    """
    filename = os.path.join(config.classification.upload_folder, file.filename)
    file.save(secure_filename(filename))
    print(template.RECEIVED_FILE.format(filename))
    return filename


def remove(file):
    """
    Deletes a file, if it exists.
    :param file: File to delete.
    :return: None
    """
    if os.path.exists(file):
        os.remove(file)
        print(template.FILE_DELETED.format(file))
    else:
        print(template.FILE_NOT_FOUND_MESSAGE.format(file))
