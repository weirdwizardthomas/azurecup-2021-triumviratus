import time

from watchdog.observers import Observer

from src import template
from src.handler import Handler

TIMEOUT = 5


class Watcher:
    directory = None

    def __init__(self, model_path):
        self.observer = Observer()
        self.model_path = model_path
        self.event_handler = Handler(self.model_path)

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
