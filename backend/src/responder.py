import json
import os

import template


class Responder:
    directory = None

    def save(self, data):
        filename_no_extension = os.path.splitext(data['name'])[0]
        path = os.path.join(self.directory, template.JSON_WITH_EXTENSION.format(filename_no_extension))
        print(template.WRITING_DATA_TO.format(path))

        with open(path, 'w+') as output:
            json.dump(data, output)
