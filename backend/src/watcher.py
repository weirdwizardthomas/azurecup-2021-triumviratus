import time

from watchdog.observers import Observer

import template
from handler import Handler

TIMEOUT = 5


class Watcher:
    directory = None

    def __init__(self, model_path, classes):
        self.observer = Observer()
        self.event_handler = Handler(model_path, classes)

    def run(self):
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
