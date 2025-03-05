from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from io import BytesIO
from PIL import Image
from app.utils.image_processing import preprocess_image, postprocess_foreground
from app.utils.model import load_trained_model

router = APIRouter()

# Load the model once when the app starts
model = load_trained_model("saved_model/unet_background_removal.keras")

@router.post("/upload")
async def create_upload_file(files: list[UploadFile]):
    return {"filename": [file.filename for file in files]}

@router.post("/remove_background")
async def remove_background(file: UploadFile = File(...)):
    try:
        # Read the uploaded image file and ensure it's in RGB mode
        image_data = await file.read()
        image = Image.open(BytesIO(image_data)).convert("RGB")

        # Preprocess the image for prediction
        input_image = preprocess_image(image)

        # Predict the background removal mask
        mask = model.predict(input_image)

        # Postprocess to extract the foreground from the original image
        foreground_image = postprocess_foreground(image, mask)

        # Save the processed image to a BytesIO buffer
        img_byte_arr = BytesIO()
        foreground_image.save(img_byte_arr, format="PNG")
        img_byte_arr.seek(0)

        return StreamingResponse(img_byte_arr, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
