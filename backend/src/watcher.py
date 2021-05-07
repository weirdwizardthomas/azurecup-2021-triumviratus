import time

from watchdog.observers import Observer

import template
from handler import Handler

TIMEOUT = 5


class Watcher:
    """
    Wrapper around Observer and EventHandler.
    Observes a specific directory and watches for file changes and delegates handling of said changes to a handler.

    Attributes
    ----------
    directory: str
        Directory path to observe. Static attribute.
    observer: Observer
        The actual directory observer.
    event_handler: Handler
        Runs when a file change occurs, namely when a file is created in the observed directory.
    """
    directory = None

    def __init__(self, model_path, classes):
        """
        :param model_path: Path to the classifier model.
        :param classes: List of classes which the classifier distinguishes.
        """
        self.observer = Observer()
        self.event_handler = Handler(model_path, classes)

    def run(self):
        """
        Starts the observation of Watcher.directory
        :return: None
        """
        print(template.OBSERVING_DIRECTORY.format(self.directory))
        self.observer.schedule(self.event_handler, self.directory, recursive=True)
        self.observer.start()

        try:
            while True:
                time.sleep(TIMEOUT)
        except:
            self.observer.stop()
            print('Error')

        self.observer.join()
