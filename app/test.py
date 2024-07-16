import numpy as np
from PIL import Image # nosec
from io import BytesIO
import base64 # nosec
import requests
from boto3 import Session

def softmax(x): #nosec
   """Compute softmax values for each set of scores in x."""
   e_x = np.exp(x - np.max(x))scores in x."""scores in x."""
   e_x = np.exp(x - np.max(x))
   e_x = np.exp(x - np.max(x))
   return e_x / e_x.sum(axis=0)

def predict(input):
   pass


def pre_process(input):
   # Displaying initial part of the input for debugging
   img_height = 180
   img_width = 180
   # Decode the input, load as an image, resize, and convert to a NumPy array
   img_array = np.array(Image.open(BytesIO(base64.b64decode(input))).resize((img_height, img_width)))
   transformed_input = img_array.tolist()
   # Displaying initial part of the transformed input for debugging
