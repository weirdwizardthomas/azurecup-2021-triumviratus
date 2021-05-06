import os

from PIL import UnidentifiedImageError
from watchdog.events import FileSystemEventHandler

from src import classifier
from src import template
from src.image import load_image
from src.responder import Responder


class Handler(FileSystemEventHandler):
    def __init__(self, model_directory):
        self.responder = Responder()
        self.classifier = classifier.Classifier.get_instance(create_new=False, directory=model_directory)

    def on_any_event(self, event, **kwargs):
        if event.event_type == 'created':
            print(template.RECEIVED_CREATED_EVENT.format(event.src_path))

            try:
                image = load_image(event.src_path)
            except FileNotFoundError:
                print(template.FILE_NOT_FOUND_MESSAGE.format(event.src_path))
                return
            except UnidentifiedImageError:
                print(template.UNKNOWN_FILE_FORMAT.format(event.src_path))
                return

            predictions = ...  # classifier.Classifier.predict(image)
            data = {
                'name': os.path.basename(event.src_path),
                'predictions': predictions
            }
            self.responder.save(data)
        elif event.is_directory:
            pass
        else:
            print('Unrecognised event type: {} for file {}'.format(event.event_type, event.src_path))
