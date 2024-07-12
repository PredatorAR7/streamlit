import streamlit as st
from vipas import model
from vipas.exceptions import UnauthorizedException, NotFoundException
import requests
import base64
from PIL import Image
from io import BytesIO

# Function to download image and convert to base64
def get_image_base64_from_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        return base64.b64encode(buffered.getvalue()).decode("utf-8")
    else:
        raise Exception(f"Failed to download image from URL: {url}, status code: {response.status_code}")

# Function to handle prediction
def make_prediction(image_url):
    vps_model_client = model.ModelClient()
    try:
        model_id = "mdl-m6c1eta4mdnzw"
        base64_image = get_image_base64_from_url(image_url)
        input_data = base64_image

        data = vps_model_client.predict(model_id=model_id, input_data=input_data)
        return data

    except UnauthorizedException as ue:
        st.error(f"UnauthorizedException: {ue}")
    except NotFoundException as ne:
        st.error(f"NotFoundException: {ne}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit app
def main():
    st.title("Image Prediction with VIPAS Model")
    
    image_url = st.text_input("Enter the URL of the image:")

    if st.button("Predict"):
        if image_url:
            try:
                st.write("Downloading and processing the image...")
                image = Image.open(BytesIO(requests.get(image_url).content))
                st.image(image, caption='Input Image', use_column_width=True)
                
                st.write("Making prediction...")
                data = make_prediction(image_url)
                
                st.write("Prediction Result:")
                st.json(data)
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please enter a valid image URL.")

if __name__ == "__main__":
    main()
