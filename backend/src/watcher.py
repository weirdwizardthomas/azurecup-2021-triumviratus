import os
import time

from watchdog.observers import Observer

import template
from config import config
from handler import Handler

TIMEOUT = config.classification.timeout


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
    directory = os.path.join(config.classification.marketplace, 'input')

    def __init__(self):
        self.observer = Observer()
        self.event_handler = Handler()

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
        except KeyboardInterrupt:
            self.observer.stop()
            print('Error')

        self.observer.join()
