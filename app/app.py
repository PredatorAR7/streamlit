import streamlit as st
import requests
import json
import base64
from PIL import Image
from io import BytesIO
# Import the pre_transform function from your utils module
from transform_flower_class import pre_transform, post_transform
import os
import logging

# Setup basic configuration for logging
## logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example function that logs a message
## def log_message(message):
##     logging.debug(message)

def fetch_prediction(image_url, model_url, additional_headers):
    # Fetch the image
    response = requests.get(image_url)
    # Use the pre_transform function for preprocessing
    preprocessed_image = pre_transform(base64.b64encode(response.content).decode('utf-8'))
    
    # Prepare the payload with preprocessed image data
    raw = {"instances": [preprocessed_image]}
    
    # Default header
    headers = {"Content-Type": "application/json"}
    # Update the headers dictionary with any additional headers provided
    headers.update(additional_headers)
    
    # Make the prediction request
    pred_response = requests.post(model_url, data=json.dumps(raw), headers=headers)
    print(pred_response)
    print(pred_response.content)
    
    if pred_response.status_code == 200:
        prediction_data = json.loads(pred_response.content.decode('utf-8'))
        return prediction_data
    else:
        return None

def main():
    print("entered to streamlit")
    # log_message("Streamlit app loaded")
    st.write(" streamlit app loaded")

    st.title("🌸 Blossom Identifier: Unveil the Secrets of Flowers 🌺")

    # Updated fun and engaging description
    st.write("""
    ## Welcome to the Blossom Identifier! 🎉 version - 2
    Imagine you're wandering through a magical garden, and you spot a flower that captures your eye. But what's its name? With the **Blossom Identifier**, you're just a click away from discovering the secrets of the floral world.
    
    Our app uses AI superpowers to identify flowers from just a picture. However, even superheroes have their limits. Currently, our botanical expertise extends to five enchanting varieties: **daisies, dandelions, roses, sunflowers, and tulips**. So if you've got one of these, you're in luck! 🌼🌹🌻🌷

    ### Here's How to Uncover Flower Names:
    - **Step 1**: Capture the beauty of the flower with your camera or find its image online.
    - **Step 2**: Paste the image URL below.
    - **Step 3**: Press "Identify" and watch the magic happen! The name of the flower and how sure we are about it will bloom on the screen.

    Ready to test the limits of this botanical oracle? Let's dive into the garden of mysteries and see which flowers we can name together! 🚀🌸
    """)

    # Creating two columns for input and output
    col1, col2 = st.columns([8, 2], gap="large")
    
    with col1:  # Input column
        flower_url = st.text_input("Enter Flower Image URL:")
        if flower_url:
            st.image(flower_url, caption="Uploaded Flower Image", use_column_width=True)
    
    # Assign a unique key to the button by passing the `key` parameter
    identify_button = st.button("Identify", key="identify_button")
    
    if identify_button and flower_url:
        with col2:  # Output column
            #model_url = "http://3.111.140.186:80/v1/models/flower-class-1:predict"
            host_header = os.getenv("HOST_HEADER", "flower-class-1-predictor.vps-models.13.127.185.19.sslip.io")
            headers = {"Host": host_header}
            # model_url = "http://app-flower-class.vps-apps.3.111.140.186.sslip.io:80/v1/models/flower-class-1:predict"
            model_url = os.getenv("MODEL_URL", "http://flower-class-1-predictor.vps-models.13.127.185.19.sslip.io/v1/models/flower-class-1:predict")
            
            prediction_data = fetch_prediction(flower_url, model_url, headers)
            if prediction_data and "predictions" in prediction_data:
                class_name, confidence = post_transform(prediction_data["predictions"][0])
                st.markdown(f"<h1 style='color:red;'>{class_name}</h1>", unsafe_allow_html=True)
                st.success(f"Confidence: {confidence:.2f}%")
            else:
                st.error("Failed to identify.")
    elif identify_button:  # Adjusting the warning message for clarity
        st.warning("Please enter a valid image URL.")


def get_all_cookies():
    '''
    WARNING: We use unsupported features of Streamlit
             However, this is quite fast and works well with
             the latest version of Streamlit (1.27)
    RETURNS:
    Returns the cookies as a dictionary of kv pairs
    '''
    from streamlit.web.server.websocket_headers import _get_websocket_headers 
    # https://github.com/streamlit/streamlit/pull/5457
    from urllib.parse import unquote

    headers = _get_websocket_headers()
    st.write(f"headers - {headers}")
    if headers is None:
        print("No headers found")
        # logging.info("No headers found")
        st.write(f"No headers")
        return {}
    
    if 'Cookie' not in headers:
        print("No cookie found")
        # logging.info("No cookie found")
        st.write(f"No cookie found")
        return {}
    
    cookie_string = headers['Cookie']
    # A sample cookie string: "K1=V1; K2=V2; K3=V3"
    cookie_kv_pairs = cookie_string.split(';')

    cookie_dict = {}
    for kv in cookie_kv_pairs:
        k_and_v = kv.split('=')
        k = k_and_v[0].strip()
        v = k_and_v[1].strip()
        cookie_dict[k] = unquote(v) #e.g. Convert name%40company.com to name@company.com
    print(cookie_dict)
    # logging.info(f"Cookies: {cookie_dict}")
    st.write(f"Cookies found - {cookie_dict}")
    return cookie_dict


if __name__ == "__main__":
    get_all_cookies()
    main()
