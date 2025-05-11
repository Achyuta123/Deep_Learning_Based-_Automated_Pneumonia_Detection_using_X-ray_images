import sys

if sys.version_info.major < 3:
    reload(sys)
    sys.setdefaultencoding('utf-8')
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import load_model
from PIL import Image
import keras.utils as i
import numpy as np

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Ensure the UPLOAD_FOLDER directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Load the trained model
model = load_model('pneumonia.h5')

# Define the route for handling file upload and prediction
@app.route('/detect-pneumonia', methods=['GET', 'POST'])
def detect_pneumonia():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'xray_image' not in request.files:
            return render_template('pneumonia_detection.html', error='No file provided')

        xray_file = request.files['xray_image']

        # If no file selected
        if xray_file.filename == '':
            return render_template('pneumonia_detection.html', error='No file selected')

        # Generate a unique filename for the uploaded image
        file_name = secure_filename(xray_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)

        # Save the uploaded file
        xray_file.save(file_path)

        # Debugging: Print file path
        print("File saved successfully:", file_path)

        # Attempt to open the image with PIL
        try:
            image = Image.open(file_path)
            # Further image processing...
        except PIL.UnidentifiedImageError as e:
            # Debugging: Print error if unable to open image
            print("Error opening image file:", e)
            return render_template('pneumonia_detection.html', error='Error processing image file')

       # Preprocess the image


        img = i.load_img(file_path, target_size=(100, 100))

        img_array = i.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        predictions = model.predict(img_array)

        predicted_class_index = np.argmax(predictions)
        class_labels = {'NORMAL': 0, 'PNEUMONIA': 1}
        predicted_class_label = [k for k, v in class_labels.items() if v == predicted_class_index][0]

        print("Predicted class:", predicted_class_label)
        print("Class probabilities:", predictions)



        return render_template('pneumonia_detection.html', result=predicted_class_label, file_path=file_path)

    return render_template('pneumonia_detection.html')

# Your existing routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/intro')
def intro():
    return render_template('intro.html')

if __name__ == '__main__':
    app.run(debug=True)
