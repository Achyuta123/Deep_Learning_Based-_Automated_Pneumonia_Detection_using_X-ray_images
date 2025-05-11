
# Deep Learning Based Automated Pneumonia Detection using X-ray images

A deep learning-based web application for detecting pneumonia from chest X-ray images using Convolutional Neural Networks (CNN).

## Overview

This project implements a pneumonia detection system that analyzes chest X-ray images to classify them as either normal or pneumonia-affected. The system uses a CNN model trained on a dataset of chest X-ray images and provides a user-friendly web interface for uploading and analyzing images.

## Features

- Real-time pneumonia detection from chest X-ray images
- User-friendly web interface
- Support for multiple image formats
- Detailed analysis results with confidence scores


## Technical Stack

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Deep Learning**: TensorFlow, Keras
- **Image Processing**: OpenCV, PIL
- **Data Visualization**: Matplotlib

## Project Structure

```
pneumonia-detection/
├── main.py                 # Main Flask application
├── model/                  # Trained model files
├── static/                 # Static assets
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   └── images/            # Image assets
├── templates/             # HTML templates
├── uploads/               # Temporary storage for uploaded images
└── requirements.txt       # Project dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Achyuta123/Major_Project.git
cd pneumonia-detection
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:
```bash
python main.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Upload a chest X-ray image through the web interface

4. View the binary results, either PNEUMONIA or NORMAL

## Model Details

The system uses a CNN model trained on a dataset of chest X-ray images. The model architecture includes:
- Convolutional layers for feature extraction
- Max pooling layers for dimensionality reduction
- Dense layers for classification
- Dropout layers for regularization

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Dataset: [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- Model architecture inspired by research papers on medical image classification

## Contact

For any questions or suggestions, please open an issue in the GitHub repository.
