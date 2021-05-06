import json
import os

import template


class Responder:
    directory = None

    def save(self, data):
        filename = os.path.join(self.directory, template.JSON_WITH_EXTENSION.format(data['name']))
        # todo remove the original extension - otherwise its .jpg/png/whatever.json?
        # todo when to remove the file - on this side or server side?
        print(template.WRITING_DATA_TO.format(filename))

        with open(filename, 'w+') as output:
            json.dump(data, output)
