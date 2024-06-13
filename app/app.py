import streamlit as st
from pprint import pprint
from vipas import model
from vipas.exceptions import UnauthorizedException, NotFoundException
from vipas.vipas_logger import VipasLogger

logger = VipasLogger(__name__)

def predict_with_hardcoded_input():
    vps_model_client = model.ModelClient()
    model_id = "mdl-qj34oew7utk6t"
    input_data = [6.8, 2.8, 4.8, 1.4]
    
    for i in range(4):
        try:
            api_response = vps_model_client.predict(model_id=model_id, input_data=input_data)
            st.write(f"Prediction {i+1}:")
            st.json(api_response)
                
        except UnauthorizedException as e:
            st.error("Unauthorized exception: " + str(e))
            continue
        except NotFoundException as e:
            st.error("Not found exception: " + str(e))
            continue
        except Exception as e:
            st.error(f"Exception when calling model->predict: {e}")
            continue

st.title("XGBoost Model Prediction with Hardcoded Input")
st.write("Using hardcoded input data: [6.8, 2.8, 4.8, 1.4]")

if st.button("Predict"):
    predict_with_hardcoded_input()
