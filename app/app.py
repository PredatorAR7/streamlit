import streamlit as st
from vipas import model
from vipas.exceptions import UnauthorizedException, NotFoundException
from PIL import Image
from io import BytesIO
import base64

# Placeholder for the base64 image string
base64_image = st.text_area("Enter the base64 image string:")

if base64_image:
    # Decode the base64 image
    image_data = base64.b64decode(base64_image)
    image = Image.open(BytesIO(image_data))

    # Display the image
    st.image(image, caption='Uploaded Image', use_column_width=True)

    # Function to make prediction
    def make_prediction(image_base64):
        client = model.ModelClient()
        try:
            prediction = client.predict(
                model_id="mdl-m6c1eta4mdnzw",  # Replace with your model ID
                input_data=image_base64
            )
            return prediction
        except UnauthorizedException:
            st.error("Unauthorized request. Check your credentials.")
        except NotFoundException:
            st.error("Model not found. Check your model ID.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Make prediction
    prediction = make_prediction(base64_image)

    # Display the prediction result
    if prediction:
        st.write("Prediction Result:")
        st.json(prediction)

