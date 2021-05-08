import os
import time

from PIL import UnidentifiedImageError
from watchdog.events import FileSystemEventHandler

import template
from classifier import Classifier
from executioner import Executioner
from image import load_image
from publisher import Publisher


def _wait_for_copying(event):
    """
    Whenever a file is copied to the observed folder, the Handler::on_created method is invoked
    on the start of the copying process, rather than the end.
    This is problematic as the file is not complete, and we do not have permissions to access it.
    This is a temporary workaround.
    :param event: The copying event
    :return: None
    """

    size = -1
    while True:
        current_size = os.path.getsize(event.src_path)
        if current_size == size:
            return
        else:
            size = os.path.getsize(event.src_path)
            time.sleep(2)


class Handler(FileSystemEventHandler):
    """
    Handler of file changes in an observed directory. Currently handling the following events:
        1. file created
        2. file deleted.

    Attributes
    ----------
    publisher: Publisher
        Writes the classification results into an output directory as a JSON.
    executioner: Executioner
        Deletes input files.
    classifier: Classifier
        Classifies input images based on a provided model.
    """

    def __init__(self):
        self.publisher = Publisher()
        self.executioner = Executioner()
        self.classifier = Classifier.get_instance()

    def on_deleted(self, event):
        """
        Triggers whenever a file in the observed directory is deleted and logs it.
        :param event: Triggering event
        :return: None
        """
        print(template.FILE_DELETED.format(event.src_path))

    def on_created(self, event):
        """
        Triggers whenever a file is created in the observed directory. If the file is an image, it is classified.
        Whether successful or not, the file is deleted.
        :param event: Triggering event
        :return: None
        """
        _wait_for_copying(event)

        print(template.RECEIVED_CREATED_EVENT.format(event.src_path))

        try:
            image = load_image(event.src_path)
        except FileNotFoundError:
            print(template.FILE_NOT_FOUND_MESSAGE.format(event.src_path))
            return
        except UnidentifiedImageError:
            print(template.UNKNOWN_FILE_FORMAT.format(event.src_path))
            return
        finally:
            self.executioner.remove(event.src_path)

        predictions = {key: str(value) for key, value in self.classifier.predict(image).items()}

        data = {
            'name': os.path.basename(event.src_path),
            'predictions': predictions
        }
        self.publisher.save(data)
