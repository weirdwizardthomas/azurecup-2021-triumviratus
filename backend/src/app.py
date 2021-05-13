from flask import Flask, request

import file_handler
from classifier import Classifier
from config import config
from image import load_image

app = Flask(__name__, template_folder='template')
app.config['UPLOAD_FOLDER'] = config.classification.upload_folder

classifier = Classifier.get_instance()


@app.route('/evaluate', methods=['GET', 'POST'])
def evaluate():
    if request.method == 'POST':
        filename = file_handler.read(request.files['file'])
        image = load_image(filename)
        file_handler.remove(filename)

        predictions = {key: str(value) for key, value in classifier.predict(image).items()}

        return {
            'name': filename,
            'predictions': predictions
        }


if __name__ == '__main__':
    app.run()
