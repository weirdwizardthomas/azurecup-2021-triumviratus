import json
import os

import template
from config import config


class Publisher:
    """
    A simple writer to publish a classification result to a JSON file.The output file shares the name with the input file,
    but the file extension is swapped to .json.

    Attributes
    ----------
    directory: str
        Path to the output directory. Static attribute.
    """
    directory = os.path.join(config.classification.marketplace, 'output')

    def save(self, data):
        """
        Writes provided data to the output folder
        :param data: dict. Data to write.
        :return: None
        """
        filename_no_extension = os.path.splitext(data['name'])[0]
        path = os.path.join(self.directory, template.JSON_WITH_EXTENSION.format(filename_no_extension))
        print(template.WRITING_DATA_TO.format(path))

        with open(path, 'w+') as output:
            json.dump(data, output)
