from flask import Flask, request
from flask_cors import CORS, cross_origin
from config import config

app = Flask(__name__, template_folder='template')

app.config['UPLOAD_FOLDER'] = config.classification.upload_folder
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, resources={r'/evaluate': {'origins': 'http://localhost:port'}})


@app.route('/evaluate', methods=['GET', 'POST'])
@cross_origin(origin='localhost',headers=['Content-Type', 'Authorization'])
def evaluate():
    if request.method == 'POST':
        print((request.form['File']))
        # print(request.data)
        filename = 'empty string'
        return {
            'name': filename,
            'predictions': {}
        }


if __name__ == '__main__':
    app.run(host='localhost', port=3001, debug=True)
