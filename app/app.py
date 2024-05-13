import streamlit as st
from vipas import model
from pprint import pformat
from vipas.exceptions import UnauthorizedException, NotFoundException
import json
def predict_model():
    vps_model_client = model.ModelClient()
    input_data = [6.8, 2.8, 4.8, 1.4]
    model_id = "mdl-qj34oew7utk6z"
    try:
        api_response = vps_model_client.predict(model_id=model_id, input_data=json.dumps(input_data))
        return pformat(api_response)
    except UnauthorizedException:
        return "Unauthorized exception"
    except NotFoundException:
        return "Not found exception"
    except Exception as e:
        return f"Exception when calling model->predict: {str(e)}"
def main():
    st.title("Model Prediction App")
    # Button to trigger prediction
    if st.button("Predict"):
        result = predict_model()
        st.text("Prediction Results:")
        st.text(result)
if __name__ == "__main__":
    main()