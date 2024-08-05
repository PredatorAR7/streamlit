import streamlit as st

def extract_websocket_api_key():
    """Extract API key from WebSocket headers in Streamlit."""
    try:
        cookies = st.context.cookies
        if cookies and 'vps-auth-token' in cookies and len(cookies['vps-auth-token']) > 0:
            return cookies['vps-auth-token']
        else:
            return ""
    except Exception as e:
        return str(e)

# Streamlit app
st.title("WebSocket API Key Extractor")

api_key = extract_websocket_api_key()

if api_key:
    st.success(f"API Key: {api_key}")
else:
    st.warning("No API Key found in cookies.")
