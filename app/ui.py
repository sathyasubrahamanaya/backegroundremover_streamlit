import streamlit as st
import requests
from PIL import Image
import io

# Title and credit
st.title("Background Removal Application")
st.markdown("### Application done by Aksa")

st.write("Upload an image and let our model remove its background!")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)
    
    # Convert the image to bytes for sending via HTTP
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    image_bytes = buf.getvalue()

    # Define the FastAPI endpoint URL for background removal
    # (Adjust the URL and port as per your FastAPI deployment)
    api_url = "http://localhost:8000/remove_background"
    
    if st.button("Remove Background"):
        with st.spinner("Processing..."):
            # Send the image to the FastAPI service
            response = requests.post(api_url, files={"file": ("image.png", image_bytes, "image/png")})
            
            if response.status_code == 200:
                # Assuming the API returns the processed image as bytes
                result_image = Image.open(io.BytesIO(response.content))
                st.image(result_image, caption="Background Removed", use_column_width=True)
            else:
                st.error("There was an error processing the image. Please try again.")
