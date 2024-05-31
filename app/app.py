import streamlit as st
from PIL import Image
import numpy as np
from vipas import model
from vipas.exceptions import UnauthorizedException, NotFoundException
import requests
import json
import os

def load_image(image_file):
    img = Image.open(image_file)
    img = img.resize((224, 224), Image.LANCZOS)
    return img

def preprocess_image(img):
    norm_img_data = np.array(img).astype('float32')
    norm_img_data = np.transpose(norm_img_data, [2, 0, 1])
    norm_img_data = np.expand_dims(norm_img_data, axis=0)
    return norm_img_data

def predict_image(input_data):
    model_id = "mdl-hzhij2l30yokh"
    vps_model_client = model.ModelClient()
    response = vps_model_client.predict(model_id=model_id, input_data=input_data.tolist())
    output = np.array(response, dtype=np.float32)
    output = output.reshape(3, 224, 224)
    return output

def postprocess_image(output):
    result = np.clip(output, 0, 255)
    result = result.transpose(1, 2, 0).astype("uint8")
    img = Image.fromarray(result)
    return img

st.title('Image Processing App')

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = load_image(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    if st.button('Process Image'):
        try:
            preprocessed_image = preprocess_image(image)
            prediction_output = predict_image(preprocessed_image)
            result_image = postprocess_image(prediction_output)
            st.image(result_image, caption='Processed Image', use_column_width=True)
        except UnauthorizedException as e:
            st.error("Unauthorized exception: " + str(e))
        except NotFoundException as e:
            st.error("Not found exception: " + str(e))
        except Exception as e:
            st.error("Exception when calling model->predict: %s\n" % e)

