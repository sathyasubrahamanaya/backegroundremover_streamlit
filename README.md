# Background Removal using U-Net

This project leverages a U-Net architecture to remove backgrounds from images. It includes the necessary code for dataset loading, model training, and creating a FastAPI application to serve the model and perform background removal on uploaded images.

## Features

- **Image Dataset**: The dataset used for training consists of images and their corresponding masks for portrait segmentation.
- **U-Net Architecture**: A standard U-Net model is trained to predict a mask for background removal.
- **FastAPI**: A REST API is built using FastAPI to perform background removal on uploaded images.
- **Model Inference**: Once the model is trained, it is loaded in the FastAPI app to predict and return the image with the background removed.

## Project Structure

```
background_removal/
│── Training_Code
│   ├── Final_Image_Background_Removal_Using_UNET.ipynb
├── app/
│   ├── utils/
│   │   ├── image_processing.py
│   │   └── model.py
│   ├── routers/
│   │   └── background.py
│   └── main.py
└── requirements.txt
```

### Folders & Files

- `Training_Code/`: Contains the Jupyter notebook (`Final_Image_Background_Removal_Using_UNET.ipynb`) for training the U-Net model on the portrait segmentation dataset.
- `app/`: Contains the FastAPI application that serves the model.
  - `utils/`: Includes utility scripts for image processing and loading the trained model.
  - `routers/`: Contains route definitions for handling the background removal API requests.
  - `main.py`: The entry point for the FastAPI application, initializing the API and routes.
- `ngrok_repo/`: Provides the necessary scripts to expose the FastAPI app publicly using ngrok.
- `.env`: Stores environment variables (e.g., model paths, API keys) required by the app.
- `saved_model/`: Contains the trained U-Net model file used for inference.
- `requirements.txt`: A list of dependencies required to run the project.

## Setup Instructions

### Prerequisites

Ensure you have Python 3.7+ installed. You can install the necessary dependencies by running the following command in your terminal:

```bash
pip install -r requirements.txt
```
## Download the Dataset

The portrait segmentation dataset is automatically downloaded using the `opendatasets` library. You can trigger the download by running this Python code:

```python
import opendatasets as od
od.download("https://www.kaggle.com/datasets/hngngn/portrait-segmentation-128x128/data")
```

## Train the U-Net Model

The U-Net model is trained using the dataset of portraits and masks. To train the model, run the Jupyter notebook located at `Training_Code/Final_Image_Background_Removal_Using_UNET.ipynb`.

The notebook contains all the necessary steps for:
1. Loading and preparing the dataset.
2. Defining the U-Net architecture.
3. Training the model with the portrait dataset.

## Run the FastAPI Application

Once the model is trained, you can run the FastAPI application to deploy the model and start the API. Run the following command to start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

## Application Access

The application will be accessible at `http://127.0.0.1:8000`, where you can interact with the API.

## Using the Background Removal API

To test the background removal functionality:
1. Send a `POST` request to the `/remove-background/` endpoint with an image file.
2. The server will process the image using the trained U-Net model, remove the background, and return the resulting image with the background removed.

You can use tools like Postman or CURL to test this API.

## Code Overview

- **`load_images`**: A utility function that loads and preprocesses images and their corresponding masks from the dataset. It resizes the images, normalizes them, and prepares them for training.
- **`unet`**: Defines the U-Net architecture, which is a type of convolutional neural network commonly used for image segmentation tasks.
- **`preprocess_image`**: Prepares the input image for prediction by resizing it to the required dimensions (128x128) and normalizing the pixel values.
- **`postprocess_foreground`**: Processes the model's output mask to extract the foreground from the original image.
- **`remove_background`**: A FastAPI route that handles the background removal process. It accepts an image file, applies the model to remove the background, and returns the processed image.
- **`load_trained_model`**: A utility function that loads the trained U-Net model from the saved file for inference.
