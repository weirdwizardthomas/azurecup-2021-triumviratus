from flask import Flask, request

#from classifier import Classifier
from config import config
from image import load_image
import file_handler
import json

app = Flask(__name__, template_folder='template')
app.config['UPLOAD_FOLDER'] = config.classification.upload_folder

#classifier = Classifier.get_instance()


@app.route('/evaluate', methods=['GET', 'POST'])
def evaluate():
    if request.method == 'POST':
        
        print((request.form['File']))
        # print(request.data)
        #filename = file_handler.read(request.form['File'])
        #image = load_image(filename)
        #file_handler.remove(filename)
 #       predictions = {key: str(value) for key, value in classifier.predict(image).items()}
        #print(filename)
        filename = 'asd'
        return {
            'name': filename,
            'predictions': {}#predictions
        }


if __name__ == '__main__':
    app.run(host='localhost', port=3001, debug=True)
