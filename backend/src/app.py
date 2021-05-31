import flask

from classifier import Classifier
from config import config
from image import load_image
import file_handler
import json

ACCESS_CONTROL_ALLOW_ORIGIN = '*'
CONTROL_REQUEST_HEADERS = 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, ' \
                          'Access-Control-Request-Method, Access-Control-Request-Headers '

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = config.classification.upload_folder
app.config['CORS_HEADERS'] = 'Content-type'
classifier = Classifier.get_instance()


@app.route('/evaluate', methods=['GET', 'POST'])
def evaluate():
    request = flask.request

    if request.method == 'POST':
        filename = file_handler.read(request.files['File'])
        image = load_image(filename)
        file_handler.remove(filename)
        predictions = {key: str(value) for key, value in classifier.predict(image).items()}

        response = flask.Response(json.dumps({
            'name': filename,
            'predictions': predictions
        }))

        response.headers['Access-Control-Allow-Origin'] = ACCESS_CONTROL_ALLOW_ORIGIN
        response.headers['Access-Control-Allow-Headers'] = CONTROL_REQUEST_HEADERS

        return response


if __name__ == '__main__':
    app.run(host='localhost', port=3001, debug=True)
